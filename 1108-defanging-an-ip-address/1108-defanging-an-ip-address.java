class Solution {
    public String defangIPaddr(String address) {
        if (address.contains(".")) {
            address = address.replace(".","[.]");
        }
        return address;
    }
}