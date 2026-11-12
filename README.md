# Automation Framework Manual

This document is a general manual for this automation.

Author: SHUBHAM KUMAR

---

## Update Before Commit

*** UPDATE FILE WITH LATEST CHANGES BEFORE COMMIT ***

---

## Base Directory

**BASE DIRECTORY must be "CSS_AUTOMATION".**

---

## Project Structure

```text
CSS_AUTOMATION/
├── resource/
│   ├── config/
│   │   ├── context.py
│   │   └── test_order.txt
│   └── test_data/
│       └── credentials.json
├── src/
│   ├── locators/
│   │   └── navigation_locators.py
│   ├── pages/
│   │   ├── base_page.py
│   │   └── navigation_page.py
│   └── utils/
├── tests/
│   ├── API/
│   ├── DB/
│   └── UI/
├── .env
├── requirements.txt
└── README.md
```

---

## Folder Details

### resource/
Keep configuration related files here.

#### config/
- `context.py`
  Contains automation basic configuration. Automation path, ENV, user config, and other related settings are in this file.

- `test_order.txt`
  List of tests. Must be updated on every change.

  Fixed format for each entry:

  ```text
  testfilename | navigation flow | author of test
  ```

  Example:

  ```text
  test_block_asset_details.py | Metering -> Inventory -> Block Storage -> Asset Details | Shubham Kumar
  ```

#### test_data/
- `credentials.json`
  Credentials JSON file.

  Important notes:
  - Do not upload to any repository.
  - .gitignore should include it.
  - Store it only on the local machine.
  - This is mandatory.

  JSON format:

  ```json
  {
    "user_role": {
      "username": "",
      "password": ""
    }
  }
  ```

---

### src/
Contains source-level framework code.

#### locators/
- `navigation_locators.py`
  Locators for navigating across CSS.

#### pages/
- `base_page.py`
  Common page actions.

- `navigation_page.py`
  Navigation-related methods.

#### utils/
- Utility files such as logger, config reader, and other helper modules should be placed here.

---

### tests/
Contains automated test suites.

- `API/`
  API tests

- `DB/`
  DB tests

- `UI/`
  Web UI tests

---

### .env
This is a mandatory file for the local environment.

It should contain environment variables and environment URLs.

---

### requirements.txt
Python packages and libraries used in this framework.

---

## Note
This README is based on the automation manual and is meant to keep the framework structure and conventions documented for the project.
