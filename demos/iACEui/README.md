# iACEui

## Interactive Autonomous Cognitive Entity User Interface

## To confirm it's working load up the API and send it a mission.  You should see something like this:

```
iaceui-api-1                 | INFO:     172.25.0.1:52132 - "POST /send-mission/ HTTP/1.1" 200 OK
iaceui-layer_1_aspirant-1    | INFO:base.base_layer:I'm the [layer_1_aspirant] and I've received a [Southbound] message, here it is: hello
iaceui-layer_2_strategist-1  | INFO:base.base_layer:I'm the [layer_2_strategist] and I've received a [Southbound] message, here it is: hello from layer_1_aspirant...
iaceui-layer_3_agent-1       | INFO:base.base_layer:I'm the [layer_3_agent] and I've received a [Southbound] message, here it is: hello from layer_2_strategist...
iaceui-layer_4_executive-1   | INFO:base.base_layer:I'm the [layer_4_executive] and I've received a [Southbound] message, here it is: hello from layer_3_agent...
iaceui-layer_5_controller-1  | INFO:base.base_layer:I'm the [layer_5_controller] and I've received a [Southbound] message, here it is: hello from layer_4_executive...
iaceui-layer_6_prosecutor-1  | INFO:__main__:I'm the [layer_6_prosecutor] and I've received a [Southbound] message, here it is: hello from layer_5_controller...
iaceui-layer_6_prosecutor-1  | INFO:__main__:I'm the [layer_6_prosecutor] and pretending have done something and sending a message [Northbound], here it is: hello from layer_5_controller...
iaceui-layer_5_controller-1  | INFO:base.base_layer:I'm the [layer_5_controller] and I've received a [Northbound] message, here it is: hello from layer_6_prosecutor...
iaceui-layer_4_executive-1   | INFO:base.base_layer:I'm the [layer_4_executive] and I've received a [Northbound] message, here it is: hello from layer_5_controller...
iaceui-layer_3_agent-1       | INFO:base.base_layer:I'm the [layer_3_agent] and I've received a [Northbound] message, here it is: hello from layer_4_executive...
iaceui-layer_2_strategist-1  | INFO:base.base_layer:I'm the [layer_2_strategist] and I've received a [Northbound] message, here it is: hello from layer_3_agent...
iaceui-layer_1_aspirant-1    | INFO:base.base_layer:I'm the [layer_1_aspirant] and I've received a [Northbound] message, here it is: hello from layer_2_strategist...
```