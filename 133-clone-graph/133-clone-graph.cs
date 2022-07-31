public class Solution {
    public Node CloneGraph(Node node) {
        
        if(node == null)
            return null;
        
        Dictionary<Node,Node> dic = new Dictionary<Node,Node>();
        dic.Add(node, new Node(node.val));
        
        dfs(node, dic);
        return dic[node];
    }
    
    private void dfs(Node node, Dictionary<Node,Node> dic)
    {
        if(node == null)
            return;
        
        foreach(var neighbor in node.neighbors)
        {
            if(!dic.ContainsKey(neighbor))
            {
                dic.Add(neighbor, new Node(neighbor.val));
                dfs(neighbor, dic);
            }
            
            dic[node].neighbors.Add(dic[neighbor]);
        }
    }
}