# 🌱 Green Experience

A desktop application that turns a hydroponic greenhouse into something you can actually see, control, and understand.

## The Problem

Running a hydroponic greenhouse means juggling dozens of moving parts at once: water pumps, pH and nutrient levels, temperature, humidity, CO2, grow lights, planting and harvest schedules, all across multiple sectors and crop lots, all changing in real time. Without a single place to see and act on this data, growers are left checking physical gauges one by one, with no early warning when something drifts out of range.

## The Approach

Green Experience is a **PyQt5 desktop simulation** of a smart greenhouse, built around a clean **Model-View-Controller** architecture:

- **Models** hold the state of every entity, sectors, lots, crops, actuators, and persist it to a local **SQLite** database.
- **Views** are PyQt5 widgets that render each entity (a pump panel, a lot's health bar, a sector overview) and stay live-updated via background `QThread` refreshers.
- **Controllers** sit between the two, translating user actions into model updates and model state into what the view displays.

The whole system runs on a **simulated, accelerated clock**: time can pass faster than real life, so crop growth, resource consumption, and equipment drift can be observed and tested without waiting weeks for a real harvest cycle.

Every actuator (pump, humidifier, temperature regulator, CO2 tank, grow lights) follows the same interface, so adding a new type of equipment means extending a common base rather than rewriting logic from scratch.

## The Result

A single application where you can:

- **Monitor the whole greenhouse at a glance**, sectors are color-coded (ok / needs attention / empty), so problems surface immediately instead of hiding in a log.
- **Drill into any sector or lot** to see live sensor readings (temperature, humidity, CO2), crop health, phenological phase, and planting/harvest dates.
- **Control actuators directly**, toggle pumps, adjust pH/EC, set target temperature, humidity, and CO2 levels, and pick the nutrient solution profile.
- **Plant and harvest lots** with one click, with yield automatically computed from crop health and timing.
- **Get proactive notifications** when an actuator is off, out of its recommended range, or when a lot is ready to harvest, needs planting, or is losing health.
- **Track consumption and productivity** over time with interactive charts (weekly / monthly / yearly / all-time).
- **Manage accounts and access**, with a full admin mode and a restricted guest mode for read-only exploration.

## Tech Stack

- **Python 3.8+**
- **PyQt5** for the GUI, `pyqtgraph` for charts, `qtwidgets` for custom controls
- **SQLite** for persistence
- Custom lightweight **MVC framework** (`util/`), singleton services, a generic `Simple_Model` / `Lista` layer for CRUD, and threaded refreshers for live UI updates

## Getting Started

### Requirements

1. Python 3.8 or later
2. The project's dependencies (see below)

### Installing dependencies

Create and activate a virtual environment, then install the requirements.

#### Windows

```
pip install virtualenv
```
```
.\venv\Scripts\activate
```
```
pip install -r requirements.txt
```

#### Linux

```
virtualenv venv
```
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```

### Running the app

```
python main.py
```

## Usage Notes

- Log in as **admin** with the credentials `user` / `pass`, or continue as **guest** for read-only access.
- To inspect or edit the database directly, install [DB Browser for SQLite](https://sqlitebrowser.org/).
- For the best experience, keep the window at its default size (1080x720) rather than resizing it.

## Project Structure

Each domain (`account`, `attuatore_generico`, `avvisi`, `centralina`, `colture`, `consumi`, `home`, `login`, `lotto`, `produttività`, `serra`, `settore`) follows the same `model / view / controller` layout, with shared infrastructure in `util/`. This consistency makes the codebase predictable to navigate, once you understand one module, you understand them all.

## Credits

Alessandro Minutillo
