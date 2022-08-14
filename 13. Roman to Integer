 int intr(char c)
    {
        int l=0;
        switch(c) {

            case 'I' :
                l=1;
                break;

            case 'V' :
                l=5;
                break;

            case 'X' :
                l=10;
                break;

            case 'L' :
                l=50;
                break;

            case 'C' :
                l=100;
                break;

            case 'D' :
                l=500;
                break;

            case 'M' :
                l=1000;
                break;

            default :
            l=0;

        }

        return l;
    }
    int romanToInt(string s) {


        int n= s.length(),x=0;

        for(int i=0;i<n;i++)
        {

            if(intr(s[i]) < intr(s[i+1]))
            {
                x-=intr(s[i]);
            }
            else
            {
                x+=intr(s[i]);


            }
        }

        return x;
    }
