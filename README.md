# damper.py

## Introduction

`damper.py` is a small library for analysing systems with viscous dampers under seismic loads. 

## Classes

### Damper

This class models a viscous damper with damping coefficient C (kN-s/m) and an exponent alpha (unitless). The method `force` returns a damping force given a relative velocity.

### Shockwave

Represents a shockwave with acceleration (m/s^2) and peak-to peak time (s). `v_max` returns maximum velocity of undamped component (m/s).

### System

Representation of a viscously damped component of a certain mass subjected to a seimic load. The damper is mounted along the axis of motion. `comp_accel` returns acceleration of component based on seimic force and apparent damping force, and `force_ratio` returns ratio of damping and seismic forces.

## Other Files

Some scripts are included to document the calculations done for our paper.