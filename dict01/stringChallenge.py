#!/usr/bin/env python3

## create three dictionary
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

challengeValue = challenge[2]
print(f"my {challengeValue[1]}! the {challengeValue[0]} do {challenge[3]}!")

trialValue = trial[2]
print(f"my {trialValue.get('goggles')}! the {trialValue.get('eyes')} do {trial[3]}!")

nightmareValue = nightmare[0]
print(f"my {nightmareValue.get('user').get('name').get('first')}! the {nightmareValue.get('kumquat')} do {nightmareValue.get('d')}!")

