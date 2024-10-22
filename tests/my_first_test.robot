*** Settings ***
Library    Browser    enable_presenter_mode=True

*** Test Cases ***
DuckDuckGo search engine is working
    [Teardown]    Close The Browser
    Open DuckDuckGo Search Engine Homepage
    Get Title    contains    DuckDuckGo
    Sleep    3s

*** Keywords ***
Open DuckDuckGo Search Engine Homepage
    Open Browser    https://duckduckgo.com/    chromium

Close The Browser
    Close Browser
