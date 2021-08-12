# Example Dashboard

A UI automation solution to Vinted dashboard using pytest and selenium.
Can be run in both the uk and de portals, more details here [Configurations](#configurations)
Multilingual platform is handled using the --cfg folder option. Another option is to use `importlib.import module` to load data files and use it instead(wasn't implemented here!)
Screenshots on failure are also implemented via the fixture `get_screenshot_on_test_failure`.
Ability to generate allure reports is also implemented, more details here [Test Reporting](#test-reporting)

#£ Versions

Python 3.6.8
pip 21.0.1

## Setup OR Installations
- Checkout the project
- Install python3
- Run ./setup.sh  (This is will install all the required dependancies)
- Run source venv/bin/activate
- Download chromedriver. Check your browser version and download a compatible driver. Example: If you are using Chrome version 87, please download ChromeDriver 87.0.4280.88
- Copy chromedriver into venv/bin/ ([Troubleshooting chromedriver setup on mac](#troubleshooting-chromedriver-setup-on-mac)))
- Setup is done


## Test Reporting 
Test report is generated using `allure-pytest`. The setup contains `/reports` dir and while running the tests are run with the tag `--alluredir reports`.
Once test is run .json files are generated in `/reports`, to view the html report, run the allure server. 
Install allure with `pip3 install allure-pytest`
Next, download the latest allure package zip file from the [https://github.com/allure-framework/allure2/releases]
    - Unzip the downloaded zip file
    - Copy the path till bin
    - Add it to the path environment variable on your local machine
    - Run `allure generate`
    - Run `allure serve <path to root project/reports/>`
    - This will open up the report in your default browser automatically and would look like the one added to the pull request

## Configurations
`/plugins/configuration.py` is setup to run the tests with different configurations. `/cfg` contains the 2 configuration files for de and uk, this allows you to run the tests on both 
portals. Use `-cfg cfg/uk_config.py tests/` to run tests using the config files.


## Folder structure

The suite is implemented using a page-object model. tests are added under `/tests` directory and objects for the 2 implemented pages are added within `/lib/page_objects` 

## Running
It is possible to run all tests on the local environment after following the above steps for setup with the following command :
  - `pytest --cfg cfg/uk_config.py tests/ --alluredir reports`
  - `to run a single test run, pytest --cfg cfg/uk_config.py tests/<name of the testfile.py> --alluredir reports`


## Troubleshooting chromedriver setup on mac
On mac verify default path, ```sudo nano /etc/paths``` is ```/usr/local/bin```. Move downloaded chromedriver to ```/usr/local/bin```. Make sure the system 'Security & Privacy' allows all externally downloaded apps to run.
