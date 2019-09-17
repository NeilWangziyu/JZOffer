
# public class Main
# {
#     public static void main(String[] args)
#     {
#         Scanner scanner = new Scanner(System.in);
#         int n = scanner.nextInt();
#         HashSet<String> set = new HashSet<String>();
#         while(n!=0)
#         {
#             char[] array = scanner.next().toCharArray();
#             Arrays.sort(array);
#             set.add(String.valueOf(array));
#             n--;
#         }
#         scanner.close();
#         System.out.println(set.size());
#     }
# }

N = int(input().strip())
hash_Set = set()
for i in range(N):
    input_str = sorted(input().strip())
    hash_Set.add(input_str)
print(len(hash_Set))
