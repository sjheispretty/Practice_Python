import csv
def save_to_file(jobs):
  print("Work is start...")
  file = open("jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "company"])
  print("Work is Doing")
  for job in jobs:
    #리스트로 값들을 출력하여라
    writer.writerow (list(job.values()))
    print ("Done")
  return