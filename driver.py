# driver.py
import subprocess

# Step 0: (Optional) Regenerate the input file if needed.
# You can run generate_input.py separately.
# Uncomment the following lines to regenerate input every time:
# subprocess.run(["python", "generate_input.py"])

# Step 1: Run the mapper on sample.txt and save output to mapped.txt
with open("input/sample.txt", "r") as infile, open("mapped.txt", "w") as mapped_out:
    subprocess.run(["python", "mapper.py"], stdin=infile, stdout=mapped_out)

# Step 2: Sort the mapper output (emulates the Shuffle and Sort phase)
# Read all lines from mapped.txt, sort them, and then write them to sorted.txt.
with open("mapped.txt", "r") as mapped_in:
    lines = mapped_in.readlines()
    lines.sort()

with open("sorted.txt", "w") as sorted_out:
    sorted_out.writelines(lines)

# Step 3: Run the reducer on sorted output to create output.txt
with open("sorted.txt", "r") as sorted_in, open("output.txt", "w") as output_out:
    subprocess.run(["python", "reducer.py"], stdin=sorted_in, stdout=output_out)

print("✅ MapReduce job completed! Check output.txt for results.")
