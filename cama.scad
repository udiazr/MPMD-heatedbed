d1=106;
d2=118;
d3=130;

r1=d1*0.5/cos(30);
r2=d2*0.5/cos(30);

r3=d3*0.5/cos(30);
echo(r2);
/*
difference(){
union(){
circle(r=r2);
    
for(i=[1:3])
    translate([r1*cos(i*120),r1*sin(i*120)])
    circle(d=7);
}
for(i=[1:3])
    translate([r1*cos(i*120),r1*sin(i*120)])
    circle(d=2.9);
}
*/


l0=[ for(i=[1:3]) [r1*cos(i*120),r1*sin(i*120)] ];

difference(){
minkowski(){
union(){
minkowski(){
polygon(l0);
circle(r=4);
}
circle(d=100);
}
circle(r=8);

}

for(i=[1:3])
    translate([r1*cos(i*120),r1*sin(i*120)])
    circle(d=0.5);


}

