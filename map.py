def color_missouri(counties, adj_counties, colors):
    """color_missouri function that takes a list of counties, a dictionary of adjacent counties,
    and a list of colors as input and prints the color assigned to each county in the Missouri map.
    """

    # Initialize an empty dictionary to store the color assigned to each county, with initial color set to None for all counties.
    color_assignment = {county: None for county in counties}

    # Invoke the color_missuri_backtrack function to assign colors to the counties in the Missouri map with the initial county index 0.
    if color_missuri_backtrack(counties, adj_counties, colors, color_assignment, 0):

        for county, color in color_assignment.items():
            print(f"County - {county} : Color - {color}")

    else:
        print("Not enough colors to color the Missouri map")


def is_safe(counties, county, adj_counties, color, color_assignment):
    """is safe function that checks if a color assigned to a county is safe or not, by taking counties list,
    current county index, adjacent counties dictionary, current color and assigned colors dictionary.

    Returns:
        bool: True if the color is safe, False otherwise.
    """

    # Check if the color is already assigned to any of the adjacent counties.
    for adj_county in adj_counties[counties[county]]:
        if color_assignment[adj_county] == color:
            return False
    return True


def color_missuri_backtrack(counties, adj_counties, colors, color_assignment, county):
    """Recursive function that uses backtracking to assign colors to the counties in the Missouri map,
    by taking list of counties, adjacent counties dictionary, list of colors, color assignment dicitonary,
    and county index as input.

    Returns:
        bool: True if the colors are assigned to all counties, False otherwise.
    """

    # If the current county index is equal to the length of counties list, then all counties are assigned a color, so return True.
    if county == len(counties):
        return True

    # Loop through all the colors and check if the color is safe to assign to the current county.
    for color in colors:

        # If the current color is safe to assign to the current county, then assign the color to the county and move to the next county.
        if is_safe(counties, county, adj_counties, color, color_assignment):
            color_assignment[counties[county]] = color

            # Recursively call the function to assign colors to the next county.
            if color_missuri_backtrack(
                counties, adj_counties, colors, color_assignment, county + 1
            ):
                return True

            color_assignment[counties[county]] = None

    return False


colors = ["Red", "Green", "Blue", "White", "Black", "Magenta", "Cyan", "Orange"]

# List of counties in Missouri.
counties = [
    "Adair",
    "Andrew",
    "Atchison",
    "Audrain",
    "Barry",
    "Barton",
    "Bates",
    "Benton",
    "Bollinger",
    "Boone",
    "Buchanan",
    "Butler",
    "Caldwell",
    "Callaway",
    "Camden",
    "Cape Girardeau",
    "Carroll",
    "Carter",
    "Cass",
    "Cedar",
    "Chariton",
    "Christian",
    "Clark",
    "Clay",
    "Clinton",
    "Cole",
    "Cooper",
    "Crawford",
    "Dade",
    "Dallas",
    "Daviess",
    "DeKalb",
    "Dent",
    "Douglas",
    "Dunklin",
    "Franklin",
    "Gasconade",
    "Gentry",
    "Greene",
    "Grundy",
    "Harrison",
    "Henry",
    "Hickory",
    "Holt",
    "Howard",
    "Howell",
    "Iron",
    "Jackson",
    "Jasper",
    "Jefferson",
    "Johnson",
    "Knox",
    "Laclede",
    "Lafayette",
    "Lawrence",
    "Lewis",
    "Lincoln",
    "Linn",
    "Livingston",
    "Macon",
    "Madison",
    "Maries",
    "Marion",
    "McDonald",
    "Mercer",
    "Miller",
    "Mississippi",
    "Moniteau",
    "Monroe",
    "Montgomery",
    "Morgan",
    "New Madrid",
    "Newton",
    "Nodaway",
    "Oregon",
    "Osage",
    "Ozark",
    "Pemiscot",
    "Perry",
    "Pettis",
    "Phelps",
    "Pike",
    "Platte",
    "Polk",
    "Pulaski",
    "Putnam",
    "Ralls",
    "Randolph",
    "Ray",
    "Reynolds",
    "Ripley",
    "Saint Charles",
    "Saint Clair",
    "Saint Francois",
    "Saint Louis",
    "Saint Louis City",
    "Sainte Genevieve",
    "Saline",
    "Schuyler",
    "Scotland",
    "Scott",
    "Shannon",
    "Shelby",
    "Stoddard",
    "Stone",
    "Sullivan",
    "Taney",
    "Texas",
    "Vernon",
    "Warren",
    "Washington",
    "Wayne",
    "Webster",
    "Worth",
    "Wright",
]

# A dictionary that maps each county with its adjacent counties.
adj_counties = {
    "Adair": ["Putnam", "Schuyler", "Scotland", "Knox", "Macon", "Linn", "Sullivan"],
    "Andrew": ["Nodaway", "Holt", "Gentry", "Dekalb", "Buchanan"],
    "Atchison": ["Nodaway", "Holt"],
    "Audrain": [
        "Randolph",
        "Monroe",
        "Ralls",
        "Pike",
        "Callaway",
        "Boone",
        "Montgomery",
    ],
    "Barry": ["McDonald", "Newton", "Lawrence", "Stone"],
    "Barton": ["Vernon", "Cedar", "Dade", "Jasper"],
    "Bates": ["Cass", "Henry", "Vernon", "Saint Clair"],
    "Benton": ["Saint Clair", "Henry", "Pettis", "Morgan", "Camden", "Hickory"],
    "Bollinger": ["Madison", "Perry", "Cape Girardeau", "Stoddard", "Wayne"],
    "Boone": [
        "Howard",
        "Randolph",
        "Audrain",
        "Callaway",
        "Cole",
        "Moniteau",
        "Cooper",
    ],
    "Buchanan": ["Andrew", "Dekalb", "Clinton", "Platte"],
    "Butler": ["Ripley", "Carter", "Wayne", "Stoddard", "Dunklin"],
    "Caldwell": ["Clinton", "Dekalb", "Daviess", "Livingston", "Carroll", "Ray"],
    "Callaway": ["Boone", "Audrain", "Montgomery", "Gasconade", "Osage", "Cole"],
    "Camden": ["Hickory", "Benton", "Morgan", "Miller", "Pulaski", "Laclede", "Dallas"],
    "Cape Girardeau": ["Perry", "Bollinger", "Stoddard", "Scott"],
    "Carroll": ["Caldwell", "Livingston", "Chariton", "Saline", "Lafayette", "Ray"],
    "Carter": ["Shannon", "Reynolds", "Wayne", "Butler", "Ripley", "Oregon"],
    "Cass": ["Jackson", "Johnson", "Henry", "Bates"],
    "Cedar": ["Vernon", "Saint Clair", "Polk", "Dade", "Barton"],
    "Chariton": [
        "Livingston",
        "Linn",
        "Macon",
        "Randolph",
        "Howard",
        "Saline",
        "Carroll",
    ],
    "Christian": ["Lawrence", "Greene", "Webster", "Douglas", "Taney", "Stone"],
    "Clark": ["Scotland", "Knox", "Lewis"],
    "Clay": ["Platte", "Clinton", "Ray", "Jackson"],
    "Clinton": ["Buchanan", "Dekalb", "Caldwell", "Ray", "Clay", "Platte"],
    "Cole": ["Moniteau", "Boone", "Callaway", "Osage", "Miller"],
    "Cooper": ["Saline", "Howard", "Boone", "Moniteau", "Morgan", "Pettis"],
    "Crawford": ["Phelps", "Gasconade", "Franklin", "Washington", "Iron", "Dent"],
    "Dade": ["Barton", "Cedar", "Polk", "Greene", "Lawrence", "Jasper"],
    "Dallas": ["Hickory", "Camden", "Laclede", "Webster", "Greene", "Polk"],
    "Daviess": ["Gentry", "Harrison", "Grundy", "Livingston", "Caldwell", "Dekalb"],
    "DeKalb": ["Andrew", "Gentry", "Daviess", "Caldwell", "Clinton", "Buchanan"],
    "Dent": ["Phelps", "Crawford", "Iron", "Reynolds", "Shannon", "Texas"],
    "Douglas": ["Christian", "Webster", "Wright", "Texas", "Howell", "Ozark", "Taney"],
    "Dunklin": ["Butler", "Stoddard", "New Madrid", "Pemiscot"],
    "Franklin": [
        "Gasconade",
        "Crawford",
        "Washington",
        "Jefferson",
        "Saint Louis",
        "Saint Charles",
        "Warren",
    ],
    "Gasconade": [
        "Callaway",
        "Montgomery",
        "Warren",
        "Franklin",
        "Crawford",
        "Phelps",
        "Maries",
        "Osage",
    ],
    "Gentry": ["Nodaway", "Worth", "Harrison", "Daviess", "DeKalb", "Andrew"],
    "Greene": ["Dade", "Polk", "Dallas", "Webster", "Christian", "Lawrence"],
    "Grundy": ["Harrison", "Mercer", "Sullivan", "Linn", "Livingston", "Daviess"],
    "Harrison": ["Gentry", "Worth", "Mercer", "Grundy", "Daviess"],
    "Henry": ["Cass", "Johnson", "Pettis", "Benton", "Saint Clair", "Bates"],
    "Hickory": ["Saint Clair", "Benton", "Camden", "Dallas", "Polk"],
    "Holt": ["Andrew", "Nodaway", "Atchison"],
    "Howard": ["Randolph", "Chariton", "Saline", "Cooper", "Boone"],
    "Howell": ["Ozark", "Douglas", "Texas", "Shannon", "Oregon"],
    "Iron": [
        "Crawford",
        "Washington",
        "Saint Francois",
        "Madison",
        "Wayne",
        "Reynolds",
        "Dent",
    ],
    "Jackson": ["Clay", "Ray", "Lafayette", "Johnson", "Cass"],
    "Jasper": ["Barton", "Dade", "Newton", "Lawrence"],
    "Jefferson": [
        "Saint Louis",
        "Franklin",
        "Washington",
        "Saint Francois",
        "Sainte Genevieve",
    ],
    "Johnson": ["Jackson", "Cass", "Henry", "Pettis", "Lafayette"],
    "Knox": ["Adair", "Scotland", "Clark", "Lewis", "Shelby", "Macon"],
    "Laclede": ["Dallas", "Camden", "Pulaski", "Texas", "Wright", "Webster"],
    "Lafayette": ["Ray", "Carroll", "Saline", "Pettis", "Johnson", "Jackson"],
    "Lawrence": ["Dade", "Greene", "Christian", "Stone", "Barry", "Newton", "Jasper"],
    "Lewis": ["Clark", "Knox", "Shelby", "Marion"],
    "Lincoln": ["Pike", "Montgomery", "Warren", "Saint Charles"],
    "Linn": ["Sullivan", "Adair", "Macon", "Chariton", "Livingston", "Grundy"],
    "Livingston": ["Daviess", "Grundy", "Linn", "Chariton", "Carroll", "Caldwell"],
    "Macon": ["Adair", "Knox", "Shelby", "Randolph", "Chariton", "Monroe"],
    "Madison": ["Iron", "Saint Francois", "Wayne", "Bollinger", "Perry"],
    "Maries": ["Miller", "Osage", "Phelps", "Gasconade", "Pulaski"],
    "Marion": ["Lewis", "Shelby", "Monroe", "Ralls"],
    "McDonald": ["Newton", "Barry"],
    "Mercer": ["Harrison", "Grundy", "Sullivan", "Putnam"],
    "Miller": ["Morgan", "Camden", "Pulaski", "Maries", "Osage", "Cole", "Moniteau"],
    "Mississippi": ["Scott", "New Madrid"],
    "Moniteau": ["Cooper", "Boone", "Cole", "Miller", "Morgan"],
    "Monroe": ["Macon", "Shelby", "Marion", "Ralls", "Audrain", "Randolph"],
    "Montgomery": [
        "Audrain",
        "Pike",
        "Lincoln",
        "Warren",
        "Gasconade",
        "Osage",
        "Callaway",
    ],
    "Morgan": ["Pettis", "Cooper", "Moniteau", "Miller", "Camden", "Benton"],
    "New Madrid": ["Mississippi", "Scott", "Stoddard", "Dunklin", "Pemiscot"],
    "Newton": ["Jasper", "Lawrence", "Barry", "McDonald"],
    "Nodaway": ["Atchison", "Holt", "Andrew", "Gentry", "Worth"],
    "Oregon": ["Howell", "Shannon", "Carter", "Ripley"],
    "Osage": ["Cole", "Callaway", "Montgomery", "Gasconade", "Maries", "Miller"],
    "Ozark": ["Taney", "Douglas", "Howell"],
    "Pemiscot": ["Dunklin", "New Madrid"],
    "Perry": [
        "Sainte Genevieve",
        "Saint Francois",
        "Madison",
        "Bollinger",
        "Cape Girardeau",
    ],
    "Pettis": ["Lafayette", "Johnson", "Henry", "Benton", "Morgan", "Cooper", "Saline"],
    "Phelps": ["Maries", "Gasconade", "Crawford", "Dent", "Texas", "Pulaski"],
    "Pike": ["Ralls", "Audrain", "Montgomery", "Lincoln"],
    "Platte": ["Buchanan", "Clinton", "Clay"],
    "Polk": ["Saint Clair", "Hickory", "Dallas", "Greene", "Dade", "Cedar"],
    "Pulaski": ["Miller", "Maries", "Phelps", "Laclede", "Camden", "Texas"],
    "Putnam": ["Mercer", "Sullivan", "Adair", "Schuyler"],
    "Ralls": ["Marion", "Monroe", "Audrain", "Pike"],
    "Randolph": ["Macon", "Shelby", "Monroe", "Audrain", "Boone", "Howard", "Chariton"],
    "Ray": ["Caldwell", "Carroll", "Lafayette", "Jackson", "Clay", "Clinton"],
    "Reynolds": ["Iron", "Dent", "Shannon", "Carter", "Wayne"],
    "Ripley": ["Oregon", "Carter", "Butler"],
    "Saint Charles": ["Lincoln", "Warren", "Franklin", "Saint Louis"],
    "Saint Clair": ["Vernon", "Bates", "Henry", "Benton", "Hickory", "Polk", "Cedar"],
    "Saint Francois": [
        "Jefferson",
        "Washington",
        "Iron",
        "Madison",
        "Perry",
        "Sainte Genevieve",
    ],
    "Saint Louis": ["Saint Charles", "Franklin", "Jefferson", "Saint Louis City"],
    "Saint Louis City": ["Saint Louis"],
    "Sainte Genevieve": ["Jefferson", "Saint Francois", "Perry"],
    "Saline": ["Carroll", "Chariton", "Howard", "Cooper", "Pettis", "Lafayette"],
    "Schuyler": ["Putnam", "Adair", "Scotland"],
    "Scotland": ["Clark", "Knox", "Schuyler", "Adair"],
    "Scott": ["Cape Girardeau", "Mississippi", "New Madrid", "Stoddard"],
    "Shannon": ["Dent", "Reynolds", "Carter", "Oregon", "Howell", "Texas"],
    "Shelby": ["Macon", "Knox", "Lewis", "Marion", "Monroe", "Randolph"],
    "Stoddard": [
        "Bollinger",
        "Cape Girardeau",
        "Scott",
        "New Madrid",
        "Dunklin",
        "Butler",
        "Wayne",
    ],
    "Stone": ["Barry", "Lawrence", "Christian", "Taney"],
    "Sullivan": ["Mercer", "Putnam", "Adair", "Macon", "Linn", "Grundy"],
    "Taney": ["Stone", "Christian", "Douglas", "Ozark"],
    "Texas": [
        "Laclede",
        "Pulaski",
        "Phelps",
        "Dent",
        "Shannon",
        "Howell",
        "Douglas",
        "Wright",
    ],
    "Vernon": ["Bates", "Saint Clair", "Cedar", "Barton"],
    "Warren": ["Lincoln", "Montgomery", "Gasconade", "Franklin", "Saint Charles"],
    "Washington": ["Franklin", "Jefferson", "Saint Francois", "Iron", "Crawford"],
    "Wayne": [
        "Madison",
        "Bollinger",
        "Stoddard",
        "Butler",
        "Carter",
        "Reynolds",
        "Iron",
    ],
    "Webster": ["Laclede", "Wright", "Douglas", "Christian", "Greene", "Dallas"],
    "Worth": ["Nodaway", "Gentry", "Harrison"],
    "Wright": ["Laclede", "Texas", "Douglas", "Webster"],
}

# Convert all counties and adjacent counties to lowercase.
counties = [county.lower() for county in counties]

# Convert all adjacent counties to lowercase.
adj_counties = {
    county.lower(): [adj_county.lower() for adj_county in adj_counties]
    for county, adj_counties in adj_counties.items()
}

# Invoke the color_missouri function to assign colors to the counties in the Missouri map.
color_missouri(counties, adj_counties, colors)
