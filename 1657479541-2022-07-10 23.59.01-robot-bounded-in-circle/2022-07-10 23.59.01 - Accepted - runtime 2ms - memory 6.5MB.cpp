class Solution {
public:
    bool isRobotBounded(string instructions) {
        int direction = 90, x=0, y=0;
        int val = 3.14/180;
        for(int i=0; i<instructions.size(); i++){
            switch(instructions[i]) {
                case 'G':
                    x += round(cos(direction*3.14/180));
                    y += round(sin(direction*3.14/180));
                    break;
                
                case 'L': direction = (direction + 90)%360; break;
                case 'R': direction = (direction - 90)%360;
            }
        }
        
        return (direction != 90 && direction != -270) || (x == 0 && y == 0);
    }   
};