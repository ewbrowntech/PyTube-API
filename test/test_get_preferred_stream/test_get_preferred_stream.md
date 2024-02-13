### get_preffered_stream()

- **[000] test_get_preffered_stream_000_nominal**
  - Conditions: v=u15tEo0wsQI | resolution = "2160p" | Streams and resolution supplied
  - Result: stream codec = vp9
- **[001] test_get_preffered_stream_001_anomalous_streams_none**
  - Conditions: streams = None
  - Result: ArgumentError("Argument 'streams' was None")
- **[002] test_get_preffered_stream_002_anomalous_streams_wrong_type**
  - Conditions: streams = "Hi"
  - Result: TypeError("Argument 'streams' must be a StreamQuery object, not <class 'str'>")
- **[003] test_get_preffered_stream_003_anomalous_resolution_none**
  - Conditions: resolution = None
  - Result: ArgumentError("Argument 'resolution' was None")
- **[004] test_get_preffered_stream_004_anomalous_resolution_wrong_type**
  - Conditions: resolution = 480
  - Result: TypeError("Argument 'resolution' must be a string, not <class 'int'> (EX: '480p')")
- **[005] test_get_preffered_stream_005_anomalous_unavailable_resolution**
  - Conditions: v=_suW-XIX_sQ | resolution = "2160p"
  - Result: UnavailableResolutionException("No stream is available at request resolution of 2160p")