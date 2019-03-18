# Prettify JSON

This script will beautify compact json data. Output will be more readebl and look pretti.

# Quickstart

You have to specify a file path with json compact data after the name of the script.

Example of script launch on Linux, Python 3.5:
```bash

$ python pprint_json.py <path to file>  # possibly requires call of python3 executive instead of jast python
{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "properties": {
                "DatasetId": 1854,
                "VersionNumber": 1,
                "ReleaseNumber": 2,
                "RowId": "79742784-9ef3-4543-bc98-a219a8903c18",
                "Attributes": {
                    "global_id": 14371450,
                    "Name": "\u0410\u0440\u043e\u043c\u0430\u0442\u043d\u044b\u0439 \u041c\u0438\u0440",
                    "IsNetObject": "\u0434\u0430",
                    "OperatingCompany": "\u0410\u0440\u043e\u043c\u0430\u0442\u043d\u044b\u0439 \u041c\u0438\u0440",
                    "TypeService": "\u0440\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043f\u0440\u043e\u0434\u043e\u0432\u043e\u043b\u044c\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0442\u043e\u0432\u0430\u0440\u043e\u0432",
                    "AdmArea": "\u0417\u0430\u043f\u0430\u0434\u043d\u044b\u0439 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u0438\u0432\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433",
                    "District": "\u0440\u0430\u0439\u043e\u043d \u041a\u0443\u043d\u0446\u0435\u0432\u043e",
                    "Address": "\u0443\u043b\u0438\u0446\u0430 \u0410\u043a\u0430\u0434\u0435\u043c\u0438\u043a\u0430 \u041f\u0430\u0432\u043b\u043e\u0432\u0430, \u0434\u043e\u043c 10",
                    "PublicPhone": [
                        {
                            "PublicPhone": "(495) 777-51-95"
                        }
                    ],
                    "WorkingHours": [
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "\u043f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a"
                        },
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "\u0432\u0442\u043e\u0440\u043d\u0438\u043a"
                        },
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "\u0441\u0440\u0435\u0434\u0430"
                        },
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "\u0447\u0435\u0442\u0432\u0435\u0440\u0433"
                        },
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "\u043f\u044f\u0442\u043d\u0438\u0446\u0430"
                        },
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "\u0441\u0443\u0431\u0431\u043e\u0442\u0430"
                        },
                        {
                            "Hours": "09:30-22:30",
                            "DayOfWeek": "\u0432\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435"
                        }
                    ],
                    "ClarificationOfWorkingHours": null
                }
            },
            "type": "Feature"
        }
    ],
    "type": "FeatureCollection"
}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
