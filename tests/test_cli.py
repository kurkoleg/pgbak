import pytest

from pgbak import cli

url='postgres://bob@example.com:5432/db_one'

@pytest.fixture
def parser():
    return cli.create_parser()


def test_parser_no_driver(parser):
    """
    CLI parser fails if no driver is specified
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])


def test_parser_with_driver(parser):
    """
    CLI parser exits if there's a driver but no destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver','local'])


def test_parser_with_unknown_driver(parser):
    """
    Driver exits if driver is not recognized (not s3 or local)
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'azure', 'destination'])


def test_parser_with_known_drivers(parser):
    """
    The Parser will work if the driver name is known good
    """
    for driver in ['local','s3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])


def test_parser_with_driver_and_destination(parser):
    """
    The parser will pass if theres both the driver and destination
    """
    args = parser.parse_args([url, '--driver','local','/some/path'])
    assert args.url == url
    assert args.driver == 'local'
    assert args.destination == '/some/path'






