turtles-own [
  energy      ;; integer
  chromosome
]

patches-own [ food ]

globals [
  max-food-amount
  cost-of-offspring
  chromosome-length
  average-fitness-f3
  average-fitness
]

to setup
  clear-all
  set max-food-amount 20 ; initial food in a new-grown patch
  set cost-of-offspring 15
  set chromosome-length 8
  ; set daily-cost-of-living 1 ;; this is on a slider now
  ask patches [
    set food 10
    set pcolor green
  ]
  create-turtles initial-turtles [
    set energy random 20
    set chromosome n-values chromosome-length [randomState]
    setxy random-xcor random-ycor
  ]
  ask turtles [
    set size 2
    recolor
  ]
  reset-ticks
end

to go
  if not any? turtles [ stop ]
  stats
  clear-links
  ask turtles with [ energy < 1 ] [ die ]
  ask turtles [ recolor ]
  ask turtles [ eat ]
  ask turtles [ move ]
  ask turtles [ set energy energy - daily-cost-of-living ]
  ask turtles [ share ]
  ask turtles [ procreate ]
  grow-grass
  tick
end

to stats
  let sumFitnessF3 0
  ask turtles [set sumFitnessF3 sumFitnessF3 + compute-f3]
  set average-fitness-f3 precision (sumFitnessF3 / population) 5

  let sumFitness 0
  ask turtles [set sumFitness energy + sumFitness]
  set average-fitness precision (sumFitness / population) 5

  ;; If calculated correctly, these should be equal
  if average-fitness-f3 != average-fitness
    [ print "ERROR: average-fitness-f3 != average-fitness" ]

end

;; move randomly
to move  ;; turtle procedure
  fd 1
  ;; turn a random amount between -40 and 40 degrees,
  ;; keeping the average turn at 0
  rt random 40
  lt random 40
end

;; eat from patch
to eat  ;; turtle procedure
  let localfood [food] of patch-here
   (ifelse
      localfood >= bitesize [
        set energy energy + bitesize
        ask patch-here [
          set food food - bitesize
          if food <= 0 [set pcolor black]
        ]
      ]
      localfood >= 0 [
        set energy energy + localfood
        ask patch-here [
          set food 0
          set pcolor black
        ]
      ])
     ; no else case
end

to procreate
  if energy > (2 * cost-of-offspring) [
    hatch 1 [
      set energy cost-of-offspring
      set color white
      mutate-chromosomes
      crossover
    ]
    set energy energy - cost-of-offspring
  ]
end

to grow-grass
  let tempGrowth new-growth
  ask patches [
    if pcolor = black [
      if tempGrowth > 0
        [ set pcolor green
          set food max-food-amount
          set tempGrowth tempGrowth - 1
        ]
  ] ]
end

; color turtles with message red, and those without message blue
to recolor  ;; turtle procedure
  ifelse energy < 10
    [ set color red ]
    [ set color blue ]
end

;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Turtle procedures ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;

to share
  if any? other turtles [
    let nearest-turtle min-one-of other turtles [distance myself]
    let energy2 [energy] of nearest-turtle
    let aid 0
    ifelse share-method = "communism"
      [ set aid share-communism energy2 ]
    [ ifelse share-method = "poll"
      [ set aid share-poll ]
    [ ifelse share-method = "proportional taxation"
      [ set aid share-prop-tax energy2 ]
      [ print "share-method not found:"
        print share-method
    ]]]

    set aid aid * (degree-of-relatedness nearest-turtle)
    ifelse aid < 0 [ print word "ERROR: aid less than 0! " (word aid) stop ]
    [ ask nearest-turtle [ set energy energy - aid ]
      set energy energy + aid
      if face-on-aid [ face nearest-turtle ]
      create-link-to nearest-turtle
    ]
  ]
end

to-report share-communism [energyOther]
  let aid (energyOther - energy) / 2
  report max list aid 0
end

to-report share-poll
  report share-poll-val
end

to-report share-prop-tax [energyOther]
  ifelse energyOther < energy [
    let looseEnergy max list (energy - share-prop-tax-theta) 0
    let aid looseEnergy * share-prop-tax-alpha
    report aid
  ]
  [ report 0 ]
end

to-report compute-f3
  let f3 0
  let i 0
  repeat length chromosome [
    let gene item i chromosome
    let presence 1
    let cf energy
    ask other turtles with [item i chromosome = gene] [
      set cf cf + energy
      set presence presence + 1
    ]
    set cf cf / presence
    set i i + 1
    set f3 f3 + cf
  ]
  set f3 f3 / i
  report f3
end

to-report degree-of-relatedness [otherTurtle]
  let i 0
  let r 0
  repeat length chromosome [
    if item i chromosome = [item i chromosome] of otherTurtle
    [ set r r + 1 ]
    set i i + 1
  ]
  report r / length chromosome
end

to-report is-sharing?
  ifelse item 0 chromosome = 1
  [ report true  ]
  [ report false ]
end

;;;;;;;;;;;;;;;;;;;;;
;;; GA procedures ;;;
;;;;;;;;;;;;;;;;;;;;;

;; As we already have procreation, I didn't use generations for this but instead
;; modified the genes of the children. As procreation requires high energy, this
;; should be fairly anlagous with taking the agents with the high fitness?

to-report population
  report count turtles
end

to mutate-chromosomes
  let j 0
  let stateBlock chromosome
  while [j < length chromosome] [
    if mutationChance > random-float 1
    [
      set stateBlock replace-item j stateBlock randomState
    ]
    set j j + 1
  ]
  set chromosome stateBlock
end

;; This is an adaption of the original crossover, it uses the children chromosomes
;; as the first set and uses a random turtle for the second agent
to crossOver
  if crossover-prob > random-float 1 [
    let otherC [chromosome] of one-of other turtles
    let slicePoint random chromosome-length
    ifelse random-float 1 > 0.5
    [ set chromosome (splitAndJoin chromosome otherC slicePoint) ] ; Sibling head
    [ set chromosome (splitAndJoin otherC chromosome slicePoint) ] ; Sibling tail
  ]
end

to-report splitAndJoin [c1 c2 slicePoint]
  let slice1 sublist c1 0 slicePoint
  let slice2 sublist c2 slicePoint chromosome-length
  report join-lists slice1 slice2
end

to-report join-lists[list1 list2]
  let jMax length list2
  let j 0
    while [j < jMax]
    [
      set list1 lput (item j list2) list1
      set j ( j + 1 )
    ]
  report list1
end


to-report randomState
  report random 2
end

; Public Domain:
; To the extent possible under law, Uri Wilensky has waived all
; copyright and related or neighboring rights to this model.
@#$#@#$#@
GRAPHICS-WINDOW
235
10
731
507
-1
-1
8.0
1
13
1
1
1
0
1
1
1
-30
30
-30
30
1
1
1
ticks
30.0

BUTTON
60
40
115
73
NIL
setup
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

BUTTON
131
40
186
73
NIL
go
T
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

BUTTON
131
40
186
73
NIL
go
T
1
T
OBSERVER
NIL
NIL
NIL
NIL
0

MONITOR
555
530
707
575
turtles
count turtles
0
1
11

PLOT
770
10
990
160
Total energy of all turtles
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -5298144 true "" "plot sum [energy] of turtles"

PLOT
771
177
971
327
Total food in patches
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot sum [food] of patches"

SLIDER
50
90
222
123
daily-cost-of-living
daily-cost-of-living
1
10
5.0
1
1
NIL
HORIZONTAL

SLIDER
50
140
222
173
initial-turtles
initial-turtles
2
100
66.0
1
1
NIL
HORIZONTAL

SLIDER
45
185
217
218
bitesize
bitesize
1
10
9.0
1
1
NIL
HORIZONTAL

CHOOSER
20
320
197
365
share-method
share-method
"communism" "poll" "proportional taxation"
0

SLIDER
25
380
197
413
share-poll-val
share-poll-val
0
20
14.8
0.2
1
NIL
HORIZONTAL

SLIDER
20
430
212
463
share-prop-tax-alpha
share-prop-tax-alpha
0
1
0.65
0.01
1
NIL
HORIZONTAL

SLIDER
20
475
207
508
share-prop-tax-theta
share-prop-tax-theta
1
50
17.0
1
1
NIL
HORIZONTAL

SLIDER
45
230
217
263
new-growth
new-growth
0
500
25.0
1
1
NIL
HORIZONTAL

PLOT
760
365
960
515
prop sharing agents
NIL
NIL
0.0
10.0
0.0
1.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot (count turtles with [is-sharing?]) / (count turtles)"

SLIDER
40
565
212
598
mutationChance
mutationChance
0
1
0.05
0.01
1
NIL
HORIZONTAL

PLOT
755
545
955
695
Average F3 Fitness
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -14070903 true "" "plot average-fitness"

SLIDER
40
605
212
638
crossover-prob
crossover-prob
0
1
0.2
0.01
1
NIL
HORIZONTAL

SWITCH
560
590
687
623
face-on-aid
face-on-aid
1
1
-1000

@#$#@#$#@
## WHAT IS IT?

This code example is a simple demo of a NetLogo simulation with patches containing food and turtles that move, eat, spend energy, reproduce (asexually) and can share food/energy with the nearest other turtle. 

A monitor keeps track of how many turtles have the message by reporting:

    count turtles 

The plot helps you visualize the overall energy of the whole population of turtles at any one time. Another plot shows how much food there is in the environment (patches).

Note that if you call a procedure inside:

    ask turtles [ ... ]

then everything in that procedure will be executed by all of the turtles.
@#$#@#$#@
default
true
0
Polygon -7500403 true true 150 5 40 250 150 205 260 250

airplane
true
0
Polygon -7500403 true true 150 0 135 15 120 60 120 105 15 165 15 195 120 180 135 240 105 270 120 285 150 270 180 285 210 270 165 240 180 180 285 195 285 165 180 105 180 60 165 15

arrow
true
0
Polygon -7500403 true true 150 0 0 150 105 150 105 293 195 293 195 150 300 150

box
false
0
Polygon -7500403 true true 150 285 285 225 285 75 150 135
Polygon -7500403 true true 150 135 15 75 150 15 285 75
Polygon -7500403 true true 15 75 15 225 150 285 150 135
Line -16777216 false 150 285 150 135
Line -16777216 false 150 135 15 75
Line -16777216 false 150 135 285 75

bug
true
0
Circle -7500403 true true 96 182 108
Circle -7500403 true true 110 127 80
Circle -7500403 true true 110 75 80
Line -7500403 true 150 100 80 30
Line -7500403 true 150 100 220 30

butterfly
true
0
Polygon -7500403 true true 150 165 209 199 225 225 225 255 195 270 165 255 150 240
Polygon -7500403 true true 150 165 89 198 75 225 75 255 105 270 135 255 150 240
Polygon -7500403 true true 139 148 100 105 55 90 25 90 10 105 10 135 25 180 40 195 85 194 139 163
Polygon -7500403 true true 162 150 200 105 245 90 275 90 290 105 290 135 275 180 260 195 215 195 162 165
Polygon -16777216 true false 150 255 135 225 120 150 135 120 150 105 165 120 180 150 165 225
Circle -16777216 true false 135 90 30
Line -16777216 false 150 105 195 60
Line -16777216 false 150 105 105 60

car
false
0
Polygon -7500403 true true 300 180 279 164 261 144 240 135 226 132 213 106 203 84 185 63 159 50 135 50 75 60 0 150 0 165 0 225 300 225 300 180
Circle -16777216 true false 180 180 90
Circle -16777216 true false 30 180 90
Polygon -16777216 true false 162 80 132 78 134 135 209 135 194 105 189 96 180 89
Circle -7500403 true true 47 195 58
Circle -7500403 true true 195 195 58

circle
false
0
Circle -7500403 true true 0 0 300

circle 2
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240

cow
false
0
Polygon -7500403 true true 200 193 197 249 179 249 177 196 166 187 140 189 93 191 78 179 72 211 49 209 48 181 37 149 25 120 25 89 45 72 103 84 179 75 198 76 252 64 272 81 293 103 285 121 255 121 242 118 224 167
Polygon -7500403 true true 73 210 86 251 62 249 48 208
Polygon -7500403 true true 25 114 16 195 9 204 23 213 25 200 39 123

cylinder
false
0
Circle -7500403 true true 0 0 300

dot
false
0
Circle -7500403 true true 90 90 120

face happy
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 255 90 239 62 213 47 191 67 179 90 203 109 218 150 225 192 218 210 203 227 181 251 194 236 217 212 240

face neutral
false
0
Circle -7500403 true true 8 7 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Rectangle -16777216 true false 60 195 240 225

face sad
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 168 90 184 62 210 47 232 67 244 90 220 109 205 150 198 192 205 210 220 227 242 251 229 236 206 212 183

fish
false
0
Polygon -1 true false 44 131 21 87 15 86 0 120 15 150 0 180 13 214 20 212 45 166
Polygon -1 true false 135 195 119 235 95 218 76 210 46 204 60 165
Polygon -1 true false 75 45 83 77 71 103 86 114 166 78 135 60
Polygon -7500403 true true 30 136 151 77 226 81 280 119 292 146 292 160 287 170 270 195 195 210 151 212 30 166
Circle -16777216 true false 215 106 30

flag
false
0
Rectangle -7500403 true true 60 15 75 300
Polygon -7500403 true true 90 150 270 90 90 30
Line -7500403 true 75 135 90 135
Line -7500403 true 75 45 90 45

flower
false
0
Polygon -10899396 true false 135 120 165 165 180 210 180 240 150 300 165 300 195 240 195 195 165 135
Circle -7500403 true true 85 132 38
Circle -7500403 true true 130 147 38
Circle -7500403 true true 192 85 38
Circle -7500403 true true 85 40 38
Circle -7500403 true true 177 40 38
Circle -7500403 true true 177 132 38
Circle -7500403 true true 70 85 38
Circle -7500403 true true 130 25 38
Circle -7500403 true true 96 51 108
Circle -16777216 true false 113 68 74
Polygon -10899396 true false 189 233 219 188 249 173 279 188 234 218
Polygon -10899396 true false 180 255 150 210 105 210 75 240 135 240

house
false
0
Rectangle -7500403 true true 45 120 255 285
Rectangle -16777216 true false 120 210 180 285
Polygon -7500403 true true 15 120 150 15 285 120
Line -16777216 false 30 120 270 120

leaf
false
0
Polygon -7500403 true true 150 210 135 195 120 210 60 210 30 195 60 180 60 165 15 135 30 120 15 105 40 104 45 90 60 90 90 105 105 120 120 120 105 60 120 60 135 30 150 15 165 30 180 60 195 60 180 120 195 120 210 105 240 90 255 90 263 104 285 105 270 120 285 135 240 165 240 180 270 195 240 210 180 210 165 195
Polygon -7500403 true true 135 195 135 240 120 255 105 255 105 285 135 285 165 240 165 195

line
true
0
Line -7500403 true 150 0 150 300

line half
true
0
Line -7500403 true 150 0 150 150

pentagon
false
0
Polygon -7500403 true true 150 15 15 120 60 285 240 285 285 120

person
false
0
Circle -7500403 true true 110 5 80
Polygon -7500403 true true 105 90 120 195 90 285 105 300 135 300 150 225 165 300 195 300 210 285 180 195 195 90
Rectangle -7500403 true true 127 79 172 94
Polygon -7500403 true true 195 90 240 150 225 180 165 105
Polygon -7500403 true true 105 90 60 150 75 180 135 105

plant
false
0
Rectangle -7500403 true true 135 90 165 300
Polygon -7500403 true true 135 255 90 210 45 195 75 255 135 285
Polygon -7500403 true true 165 255 210 210 255 195 225 255 165 285
Polygon -7500403 true true 135 180 90 135 45 120 75 180 135 210
Polygon -7500403 true true 165 180 165 210 225 180 255 120 210 135
Polygon -7500403 true true 135 105 90 60 45 45 75 105 135 135
Polygon -7500403 true true 165 105 165 135 225 105 255 45 210 60
Polygon -7500403 true true 135 90 120 45 150 15 180 45 165 90

square
false
0
Rectangle -7500403 true true 30 30 270 270

square 2
false
0
Rectangle -7500403 true true 30 30 270 270
Rectangle -16777216 true false 60 60 240 240

star
false
0
Polygon -7500403 true true 151 1 185 108 298 108 207 175 242 282 151 216 59 282 94 175 3 108 116 108

target
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240
Circle -7500403 true true 60 60 180
Circle -16777216 true false 90 90 120
Circle -7500403 true true 120 120 60

tree
false
0
Circle -7500403 true true 118 3 94
Rectangle -6459832 true false 120 195 180 300
Circle -7500403 true true 65 21 108
Circle -7500403 true true 116 41 127
Circle -7500403 true true 45 90 120
Circle -7500403 true true 104 74 152

triangle
false
0
Polygon -7500403 true true 150 30 15 255 285 255

triangle 2
false
0
Polygon -7500403 true true 150 30 15 255 285 255
Polygon -16777216 true false 151 99 225 223 75 224

truck
false
0
Rectangle -7500403 true true 4 45 195 187
Polygon -7500403 true true 296 193 296 150 259 134 244 104 208 104 207 194
Rectangle -1 true false 195 60 195 105
Polygon -16777216 true false 238 112 252 141 219 141 218 112
Circle -16777216 true false 234 174 42
Rectangle -7500403 true true 181 185 214 194
Circle -16777216 true false 144 174 42
Circle -16777216 true false 24 174 42
Circle -7500403 false true 24 174 42
Circle -7500403 false true 144 174 42
Circle -7500403 false true 234 174 42

turtle
true
0
Polygon -10899396 true false 215 204 240 233 246 254 228 266 215 252 193 210
Polygon -10899396 true false 195 90 225 75 245 75 260 89 269 108 261 124 240 105 225 105 210 105
Polygon -10899396 true false 105 90 75 75 55 75 40 89 31 108 39 124 60 105 75 105 90 105
Polygon -10899396 true false 132 85 134 64 107 51 108 17 150 2 192 18 192 52 169 65 172 87
Polygon -10899396 true false 85 204 60 233 54 254 72 266 85 252 107 210
Polygon -7500403 true true 119 75 179 75 209 101 224 135 220 225 175 261 128 261 81 224 74 135 88 99

wheel
false
0
Circle -7500403 true true 3 3 294
Circle -16777216 true false 30 30 240
Line -7500403 true 150 285 150 15
Line -7500403 true 15 150 285 150
Circle -7500403 true true 120 120 60
Line -7500403 true 216 40 79 269
Line -7500403 true 40 84 269 221
Line -7500403 true 40 216 269 79
Line -7500403 true 84 40 221 269

x
false
0
Polygon -7500403 true true 270 75 225 30 30 225 75 270
Polygon -7500403 true true 30 75 75 30 270 225 225 270
@#$#@#$#@
NetLogo 6.3.0
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
default
0.0
-0.2 0 0.0 1.0
0.0 1 1.0 0.0
0.2 0 0.0 1.0
link direction
true
0
Line -7500403 true 150 150 90 180
Line -7500403 true 150 150 210 180
@#$#@#$#@
1
@#$#@#$#@
