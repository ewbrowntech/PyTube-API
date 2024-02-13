### get_streams()

- **[000] test_get_streams_000_nominal**
  - Conditions: v=SOI4OF7iIr4
  - Result: Streams resturned
- **[001] test_get_streams_001_anomalous_no_input**
  - Conditions: youtube = None
  - Result: ArgumentError("Argument 'youtube' was None")
- **[002] test_get_streams_002_anomalous_input_wrong_type**
  - Conditions: youtube = "Hi"
  - Result: TypeError("Argument 'youtube' must be a YouTube object")
- **[003] test_get_streams_003_anomalous_age_restricted**
  - Conditions: v=95_33ItUC9k | Video is age restricted
  - Result: HTTPException("401: 95_33ItUC9k is age restricted, and can't be accessed without logging in.")
