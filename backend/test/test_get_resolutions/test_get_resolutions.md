### get_resolutions()

- **[000] test_get_resolutions_000_nominal**
  - Conditions: v=SOI4OF7iIr4 | Streams supplied
  - Result: resolutions = ["1080p", "720p", "480p", "360p", "240p", "144p"]
- **[001] test_get_resolutions_001_anomalous_no_input**
  - Conditions: streams = None
  - Result: ArgumentError("Argument 'streams' was None")
- **[002] test_get_resolutions_002_anomalous_input_wrong_type**
  - Conditions: streams = "Hi"
  - Result: TypeError("Argument 'streams' must be a StreamQuery object")
