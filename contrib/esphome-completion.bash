#!/bin/env/bash
ESPHOME_COMMANDS=(config compile upload logs discover run clean-mqtt wizard mqtt-fingerprint version clean dashboard rename)
_esphome_completions()
{
  if [[ ${ESPHOME_COMMANDS[@]} =~ $3 ]]; then
    COMPREPLY=( *.yaml )
  else
    COMPREPLY=( $(compgen -W "${ESPHOME_COMMANDS[*]}" -- $2))
  fi
}

complete -F _esphome_completions esphome
