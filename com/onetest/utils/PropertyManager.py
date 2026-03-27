from jproperties import Properties

p = Properties()
with open("/home/bazzite/devhome/projects/onetest-selenium/config.properties", "rb") as f:
    p.load(f, encoding="utf-8")

def get_property_value(key: str) -> str:
    if not p[key][0]:
        raise ValueError("Error getting property value")
    else:
        return p[key][0]

def is_healing_enabled() -> bool:
    return p['healing.enabled'][0] == 'true'