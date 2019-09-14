def count(lst):
  count={}
  for item in lst:
    try:
      count[item]+=1
    except(KeyError):
      count[item]=1
  return count
  
def main():
  n_cand=input()
  n_cand=[int(i) for i in n_cand.split(' ')]
  all_voted=[]
  for i in range(5):
    temp=input()
    temp=[int(i) for i in temp.split(' ')]
    all_voted.append(temp)
  all_voted = [item for sublist in all_voted for item in sublist]
  all_voted=sorted(all_voted)
  n_candidates_elected=0
  ct=count(all_voted)
  for n_zones in ct.values():
    if n_zones>=3:
      n_candidates_elected+=1
  print(n_candidates_elected)
  return 0

if __name__ == '__main__':
  main()
