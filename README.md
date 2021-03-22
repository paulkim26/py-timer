# py-timer

## Introduction
`py-timer` is a configurable Python script that displays an on-screen timer. Uses the `pygame` set of modules to render the timer text. Includes controls to pause, play, reset, and fast forward the timer.

Great for tracking the time remaining in events such as:
- Escape rooms
- Examinations
- Competitions

Shows the time remaining as `mm:ss:hhh` where:
- `mm` is the minutes remaining
- `ss` is the seconds
- `hhh` is the milliseconds

## Requirements
- python `v3.7.7`
- [pygame](www.pygame.org) `v1.9.4` or higher ([installation instructions](https://www.pygame.org/wiki/GettingStarted))

## Setup
Requires an OTF font to be installed for rendering the timer text. The suggested font is [Digital Dismay](https://www.dafont.com/digital-dismay.font).

## Configuration
| Variable | Description |
| - | - |
| `time_limit` | The number of minutes to count down from. |
| `update_frequency` | The frequency in seconds to update the timer. If `0` will update as fast as possible. Higher values are more performant. |
| `font_path` | The file directory path to the installed OTF font. |
| `font_size` | Size of the text to be rendered. |
| `screen_width` | Horizontal window size. |
| `screen_height` | Vertical window size. |
| `screen_fullscreen` | Determines whether to render the timer in fullscreen or not. |

## Run
```
python timer.py
```

## Controls
| Key | Description |
| - | - |
| `escape` | Exits the program. |
| `space` | Pause/play the timer. |
| `r` | Reset the timer. |
| `left` | Skip backwards 1 minute. |
| `right` | Skip forwards 1 minute. |
| `shift` | Modifies `left` and `right` keys to skip 3 minutes at a time. |
