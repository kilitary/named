---
promptId: completeTex t Bloom
name: 🪄 Complete Text using Bloom Model
description: select considered context and run the command
author: Noureddinne
tags: huggingface, text, bloom
version: 0.0.1
provider: hf
model: bigscience/bloom
state: Focus
---
{{select io n}}

| model | version | layers | secured8 | comment      | departing_delay | lifetime     |
| ----- | ------- | ------ | -------- | ------------ | --------------- | ------------ |
| 0001  | 0001    | 2      | no       | alpha(labs)  | 1 day           | continueable |
| 0003  | 0001    | 3      | no       | alpha(alpha) | only local      | test fail    |
|       |         |        |          |              |                 |              |
