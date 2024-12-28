# Amharic rows data structure
amharic_rows = {
    "ሀ": "ሀሁሂሃሄህሆ",
    "ለ": "ለሉሊላሌልሎ",
    "ሐ": "ሐሑሒሓሔሕሖ",
    "መ": "መሙሚማሜምሞ",
    "ሠ": "ሠሡሢሣሤሥሦ",
    "ረ": "ረሩሪራሬርሮ",
    "ሰ": "ሰሱሲሳሴስሶ",
    "ሸ": "ሸሹሺሻሼሽሾ",
    "ቀ": "ቀቁቂቃቄቅቆ",
    "በ": "በቡቢባቤብቦ",
    "ተ": "ተቱቲታቴትቶ",
    "ቸ": "ቸቹቺቻቼችቾ",
    "ኀ": "ኀኁኂኃኄኅኆ",
    "ነ": "ነኑኒናኔንኖ",
    "ኘ": "ኘኙኚኛኜኝኞ",
    "አ": "አኡኢኣኤእኦ",
    "ከ": "ከኩኪካኬክኮ",
    "ኸ": "ኸኹኺኻኼኽኾ",
    "ወ": "ወዉዊዋዌውዎ",
    "ዐ": "ዐዑዒዓዔዕዖ",
    "ዘ": "ዘዙዚዛዜዝዞ",
    "ዠ": "ዠዡዢዣዤዥዦ",
    "የ": "የዩዪያዬይዮ",
    "ደ": "ደዱዲዳዴድዶ",
    "ጀ": "ጀጁጂጃጄጅጆ",
    "ገ": "ገጉጊጋጌግጎ",
    "ጠ": "ጠጡጢጣጤጥጦ",
    "ጨ": "ጨጩጪጫጬጭጮ",
    "ጰ": "ጰጱጲጳጴጵጶ",
    "ጸ": "ጸጹጺጻጼጽጾ",
    "ፀ": "ፀፁፂፃፄፅፆ",
    "ፈ": "ፈፉፊፋፌፍፎ",
    "ፐ": "ፐፑፒፓፔፕፖ",
    "ቨ": "ቨቩቪቫቬቭቮ"
}

# Step 1: Preprocess to create a grid mapping of each character to (row, column)
amharic_grid = {}
for row_index, (base_char, row) in enumerate(amharic_rows.items()):
    for col_index, char in enumerate(row):
        amharic_grid[char] = (row_index, col_index)
# print (amharic_grid)
# Step 2: Function to calculate Manhattan Distance between two characters
def manhattan_distance(char1, char2):
    row1, col1 = amharic_grid[char1]
    row2, col2 = amharic_grid[char2]
    return abs(row1 - row2) + abs(col1 - col2)

# Step 3: Function to calculate cumulative average Manhattan distance for a word
def average_manhattan_distance(word):
    total_distance = 0
    num_pairs = 0
    for i in range(len(word)):
        for j in range(i + 1, len(word)):  # Only consider pairs (i, j) where i < j
            total_distance += manhattan_distance(word[i], word[j])
            num_pairs += 1
    return total_distance / num_pairs if num_pairs > 0 else 0

# Step 4: Sort words based on cumulative average Manhattan distance
def sort_words_by_distance(words):
    word_distances = [(word, average_manhattan_distance(word)) for word in words]
    sorted_words = sorted(word_distances, key=lambda x: x[1])
    return [word for word, _ in sorted_words]

# Step 5: Input words, calculate distances, and print in order
words = ["ዤል", "ለሊሴ", "ቦንቱ", "ፎዝያ"]  # Replace with input if desired
sorted_words = sort_words_by_distance(words)
print("Sorted words by cumulative average Manhattan distance:")
for word in sorted_words:
    print(word)
