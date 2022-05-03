class Solution
{
public:
	bool isMatch(string s,string p)
	{
		int m = s.size();
		int n = p.size();
		int i = 0,j=0;
		int matchI = -1,starJ = -1;
		while(i<m)
		{
			if(j<n && p[j]=='*')
			{
				matchI = i;
				starJ = j;
				j++;

			}
			else if(j<n &&(p[j] == '?' || p[j] == s[i]))
			{
				i++;
				j++;
			}
			else if(starJ >-1)
			{
				i = matchI+1;
				j = starJ+1;
				matchI++;

			}
			else return false;
		}

		while(j<n && p[j] == '*') j++;

		return j ==n;
	}
};