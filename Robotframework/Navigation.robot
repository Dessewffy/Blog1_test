*** Settings ***
# Use Selenium WebDriver and Applitools Eyes.
Library     Selenium2Library



# Declare setup and teardown routines.
Test Setup        Setup
Test Teardown

*** Variables ***
#Declare variables and lists. LOGIN-Credentials are in a list.
${LOGIN-BUTTON}     //li[@routerlink="login"]
${URL}      http://ec2-3-120-40-183.eu-central-1.compute.amazonaws.com


@{LOGIN-Credentials-USER}

*** Keywords ***
# For setup, load the site main page and open Eyes to start visual testing.
Setup
    Open Browser    ${URL}      chrome
    Maximize Browser Window
    Title Should Be    title=Blog1Project


Login_USER
    Click Element       ${LOGIN-BUTTON}
    Input Text          //input[@type="text"]                       Alysha.Hahn98

