## Setup

1. Create a virtual enviroment to install the necessary libraries:

```bash
python -m venv autominer-env
```

2. Activate the virtual enviroment:

On Mac OS:
```bash
source autominer-venv/bin/activate
```

On Windows:
```bash
autominer-venv\Scripts\activate.bat
```

3. Install the required libraries:

```bash
pip install Pillow PyAutoGUI 
```

4. Run script:

```bash
python main.py
```

5. Quickly move to the Club Penguin Client screen and let the script do it's job.

## Variables

You can adjust any variable as needed according to your needs.

|       Variable       | Type   | Description                                                                                                                        | Format                           | Default value                           |
|:--------------------:|--------|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|-----------------------------------------|
| GROUND_COLORS        | List   | List of rgba colors of the ground of the mining region. Used to make sure the bot is clicking on the ground and not anywhere else. | [(red, green, blue, alpha), ...] | [(103, 80, 76, 255), (94, 70, 67, 255)] |
| MINPOINT             | Tuple  | Coordinates for the minimum point of the desired mining region.                                                                    | (x, y)                           | (840, 700)                              |
| MAXPOINT             | Tuple  | Coordinates for the maximum point of the desired mining region.                                                                    | (x, y)                           | (960, 870)                              |
| MINING_TIME          | Double | Time spent mining before moving on to another spot.                                                                                | seconds                          | 30                                      |
| AVERAGE_WALKING_TIME | Double | Time the penguin spends moving to another spot. Used to wait before it starts to mine again.                                       | seconds                          | 2.5                                     |

## Troubleshooting

