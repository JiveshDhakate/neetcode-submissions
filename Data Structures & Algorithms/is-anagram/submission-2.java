class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false; 
        }
        char[] sstr=s.toCharArray();
        char[] tstr=t.toCharArray();
        Arrays.sort(sstr);
        Arrays.sort(tstr);
        String sorted_s=new String(sstr);
        String sorted_t=new String(tstr);

        if(sorted_s.equals(sorted_t)){
            return true;
        }
        else{
            return false;
        }

    }
}
