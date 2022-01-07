import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.core import CORE, coroutine_with_priority

from esphome.const import (
    CONF_ENABLE_IPV6,
)

CODEOWNERS = ["@esphome/core"]
AUTO_LOAD = ["mdns"]

network_ns = cg.esphome_ns.namespace("network")
IPAddress = network_ns.class_("IPAddress")

NetworkComponent = network_ns.class_("WiFiComponent", cg.Component)

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(NetworkComponent),
            cv.Optional(CONF_ENABLE_IPV6): cv.boolean,
        }
    ),
)


@coroutine_with_priority(60.0)
async def to_code(config):

    if CONF_ENABLE_IPV6 in config and config[CONF_ENABLE_IPV6]:
        cg.add_build_flag("-DCONFIG_LWIP_IPV6")
        cg.add_build_flag("-DCONFIG_LWIP_IPV6_AUTOCONFIG")
        if CORE.is_esp8266:
            cg.add_build_flag("-DPIO_FRAMEWORK_ARDUINO_LWIP2_IPV6_LOW_MEMORY")
