# pretty-log-tools
A set of tools to color and format logging using Unix pipes

# tl;dr
```
export PRETTY_LOG_TOOLS_FOLDER='~/<path>/pretty-log-tools'
source "~/<path>/pretty-log-tools/source"
```
```tail -f mylogfile | prettyId```

# Description
This folder adds a few aliases that can be used in pipes.
Just add in your bash/zshrc/... the following:
```source <path>/pretty-log-tools/source```


Available aliases:
- prettyLevel:
  - color DEBUG, INFO, WARNING, ERROR, CRITICAL words with relevant colors.
- prettyDate:
  - color date whose format match: `YYYY:MM:DD hh:mm:ss,uuu`
- prettySource:
  - group sources (between `[` `]`) with the same colors
- prettyId:
  - highlight ids of 8 hexa characters or UUID format (8x-4x-4x-4x-12x)
- prettyJson:
  - try to prettify dict or json representations within the logs.
