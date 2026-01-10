// Vertex shader - particle animation 

#version 430 core

layout(location = 0) in float in_center_x;
layout(location = 1) in float in_center_y;
//layout(location = 2) in float in_velocity_x;
//layout(location = 3) in float in_velocity_y;
//layout(location = 4) in float in_acceleration_x;
//layout(location = 5) in float in_acceleration_y;
layout(location = 6) in float in_color_r;
layout(location = 7) in float in_color_g;
layout(location = 8) in float in_color_b;
layout(location = 9) in float in_color_a;
layout(location = 10) in float in_point_size;

uniform vec2 resolution;

out vec4 v_color;  

void main()
{
    gl_Position = vec4(in_center_x, in_center_y, 0.0, 1.0);
    
    // Korrektur der PointSize (wie wir besprochen haben)
    gl_PointSize = in_point_size;  // direkte Pixelgröße, keine Multiplikation mit resolution.x!

    v_color = vec4(in_color_r, in_color_g, in_color_b, in_color_a);
}
