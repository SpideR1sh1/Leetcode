class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> ans=new LinkedList<>();
        int m=heights.length,n=heights[0].length;
        boolean[][] visPacific=new boolean[m][n],visAtlantic=new boolean[m][n];
        Queue<int[]> queuePacific=new LinkedList<>(),queueAtlantic=new LinkedList<>();
        for(int i=0;i<m;i++)
        {
            visPacific[i][0]=true;
            visAtlantic[i][n-1]=true;
            queuePacific.offer(new int[]{i,0});
            queueAtlantic.offer(new int[]{i,n-1});
        }
        for(int i=0;i<n;i++)
        {
            visPacific[0][i]=true;
            visAtlantic[m-1][i]=true;
            queuePacific.offer(new int[]{0,i});
            queueAtlantic.offer(new int[]{m-1,i});
        }
        bfs(queuePacific,visPacific,heights,m,n);
        bfs(queueAtlantic,visAtlantic,heights,m,n);
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(visPacific[i][j]&&visAtlantic[i][j])
                {
                    List<Integer> temp=new LinkedList<>();
                    temp.add(i);
                    temp.add(j);
                    ans.add(temp);
                }
            }
        }
        return ans;
    }
    void bfs(Queue<int[]> queue,boolean[][] vis,int[][] heights,int m,int n)
    {
        int[][] dirs={{1,0},{-1,0},{0,1},{0,-1}};
        while(!queue.isEmpty())
        {
            int[] curr=queue.poll();
            for(int[] dir:dirs)
            {
                int newX=curr[0]+dir[0];
                int newY=curr[1]+dir[1];
                if(newX>=0&&newY>=0&&newX<m&&newY<n&&!vis[newX][newY]
                   &&heights[curr[0]][curr[1]]<=heights[newX][newY])
                {
                    vis[newX][newY]=true;
                    queue.offer(new int[]{newX,newY});
                }
            }
        }
    }
}