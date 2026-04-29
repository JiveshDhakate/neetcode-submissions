class Solution {
    public boolean isAnagram(String s, String t) {
        // if (s.length() != t.length()) {
        //     return false; 
        // }
        // char[] sstr=s.toCharArray();
        // char[] tstr=t.toCharArray();
        // Arrays.sort(sstr);
        // Arrays.sort(tstr);
        // String sorted_s=new String(sstr);
        // String sorted_t=new String(tstr);

        // if(sorted_s.equals(sorted_t)){
        //     return true;
        // }
        // else{
        //     return false;
        // }
        if (s.length() != t.length()) {
            return false; // If the lengths are different, they cannot be anagrams
        }

        HashMap<Character,Integer> hashmap=new  HashMap<>();
        
        for(int i=0;i<s.length();i++){
            char ch= s.charAt(i);
            hashmap.put(ch,hashmap.getOrDefault(ch,0)+1);
        }
        for(int i=0;i<t.length();i++){
            char ch= t.charAt(i);
            if(!hashmap.containsKey(ch)){
                return false;
            }
            else{
                hashmap.put(ch,hashmap.get(ch)-1);
            }
        }
        for(int i: hashmap.values()){
            if(i!=0){
                return false;
            }
        }
        return true;
        
        


    }
}
