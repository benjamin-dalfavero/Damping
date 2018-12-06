# damper.py

## Introduction

`Damper.py` is a small library for analysing systems with viscous dampers under seismic loads. 

## Classes

### Damper

This class models a viscous damper with damping coefficient C (kN-s/m) and an exponent alpha (unitless). The method `force` returns a damping force given a relative velocity.