Feature: SDET assignment - Chrome Extension Automated Testing

    Scenario: Test one of the feature of the extension - Google Dictionary
        Given User adds the extension and opens the browser
        When User navigates to the popup page of the extension
        And User enter word and search for the definition
        Then User verify the definititon is found and close the browser

    Scenario: Test the options page of the extension - Google Dictionary
        Given User adds the extension and opens the browser
        When User navigates to the options page of the extension
        And User modify the languages setting of the extension
        And User opens new tab
        And User navigates to the popup page of the extension
        And User enter word and search for the definition
        Then User verify the definititon is found and close the browser

