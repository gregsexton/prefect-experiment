from prefect import flow, task
from prefect.logging import get_run_logger
import random

@task
def process_fizz(x):
    logger = get_run_logger()
    logger.info('fizz')
    if x % 3 == 0:
        process_quux(x);

@task
def process_buzz(x):
    logger = get_run_logger()
    logger.info('buzz')
    if x % 3 == 0:
        process_baz(x)

@task
def process_baz(x):
    logger = get_run_logger()
    logger.info('baz')

@task
def process_quux(x):
    logger = get_run_logger()
    logger.info('quux')

@flow
def main(x: int) -> list[str]:
    if x % 2 == 0:
        process_fizz(x)
    else:
        process_buzz(x)
    return []


if __name__ == "__main__":
    main(9)
