"""Constants for Visual Crossing Weather component."""

from homeassistant.components.weather import (
    ATTR_CONDITION_CLEAR_NIGHT,
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_FOG,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SNOWY_RAINY,
    ATTR_CONDITION_SUNNY,
    ATTR_CONDITION_WINDY,
)

ATTR_DESCRIPTION = "description"
ATTR_LAST_UPDATED = "last_updated"
ATTR_DATETIMEEPOCH = "datetimeepoch"
ATTR_SNOW = "snow"
ATTR_SNOW_DEPTH = "snow_depth"
ATTR_PRECIPITATION_TYPE = "precipitation_type"
ATTR_SOLAR_RADIATION = "solar_radiation"
ATTR_SOLAR_ENERGY = "solar_energy"
ATTR_SEVERE_RISK = "severe_risk"
ATTR_SUNRISE = "sunrise"
ATTR_SUNSET = "sunset"
ATTR_MOONPHASE = "moonphase"

CONF_UNIT_GROUP = "unitgroup"
CONF_TIMEZONE = "time_zone"

CONF_DAYS = "days"

DEFAULT_DAYS = 7
DEFAULT_LANGUAGE = "en"
DEFAULT_UNIT_GROUP = "uk"
DEFAULT_NAME = "Home"
DOMAIN = "visualcrossing"

CONDITIONS_MAP = {
    ATTR_CONDITION_CLEAR_NIGHT: {"clear-night"},
    ATTR_CONDITION_CLOUDY: {"cloudy"},
    ATTR_CONDITION_FOG: {"fog"},
    ATTR_CONDITION_LIGHTNING_RAINY: {
        "thunder-rain",
        "thunder-showers-day",
        "thunder-showers-night",
    },
    ATTR_CONDITION_PARTLYCLOUDY: {
        "partly-cloudy-day",
        "partly-cloudy-night",
    },
    ATTR_CONDITION_POURING: {"heavy-rain"},
    ATTR_CONDITION_RAINY: {"rain", "showers-day", "showers-night"},
    ATTR_CONDITION_SNOWY: {
        "snow",
        "snow-showers_day",
        "snow-showers_night",
        "snow-showers-day",
        "snow-showers-night",
    },
    ATTR_CONDITION_SNOWY_RAINY: {
        "sleet",
        "sleet-day",
        "sleet-night",
    },
    ATTR_CONDITION_SUNNY: {"clear-day"},
    ATTR_CONDITION_WINDY: {"wind"},
}
