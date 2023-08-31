import random

# Sample data for demonstration
import random


def getFirstName():
    first_name = [
        "Noah", "Liam", "William", "James", "Oliver", "Benjamin", "Elijah", "Lucas", "Mason", "Logan",
        "Alexander", "Ethan", "Jacob", "Michael", "Daniel", "Henry", "Jackson", "Sebastian", "Aiden", "Matthew",
        "Samuel", "David", "Joseph", "Carter", "Owen", "Wyatt", "John", "Jack", "Luke", "Andrew",
        "Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn",
        "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Avery", "Sofia", "Camila", "Aria", "Scarlett",
        "Victoria", "Madison", "Luna", "Grace", "Chloe", "Penelope", "Layla", "Riley", "Zoey", "Nora"
    ]
    return first_name


def getLastName():
    last_name = [
        "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
        "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
        "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King",
        "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter",
        "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins"
    ]
    return last_name


def getStates():
    states = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
        "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
        "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
        "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
        "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
        "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
        "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ]
    return states


def getParties():
    parties = ["Progressive Alliance Party", "National Unity Party", "Civic Renewal Party", "Independant"]
    return parties

def getCandidates():
    candidates = ["Elizabeth Foster", "Robert Johnson", "Sarah Thomas"]
    return candidates

def getStateCandidates():
    state_candidates = {
        "Alabama": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Alaska": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Arizona": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Arkansas": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "California": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Colorado": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Connecticut": ["Robert Johnson", "Elizabeth Foster", "Sarah Thomas"],
        "Delaware": ["Robert Johnson", "Elizabeth Foster", "Sarah Thomas"],
        "Florida": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Georgia": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Hawaii": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Idaho": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Illinois": ["Sarah Thomas", "Elizabeth Foster", "Robert Johnson"],
        "Indiana": ["Sarah Thomas", "Elizabeth Foster", "Robert Johnson"],
        "Iowa": ["Sarah Thomas", "Elizabeth Foster", "Robert Johnson"],
        "Kansas": ["Sarah Thomas", "Elizabeth Foster", "Robert Johnson"],
        "Kentucky": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Louisiana": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Maine": ["Robert Johnson", "Elizabeth Foster", "Sarah Thomas"],
        "Maryland": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Massachusetts": ["Robert Johnson", "Elizabeth Foster", "Sarah Thomas"],
        "Michigan": ["Sarah Thomas", "Elizabeth Foster", "Robert Johnson"],
        "Minnesota": ["Sarah Thomas", "Elizabeth Foster", "Robert Johnson"],
        "Mississippi": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Missouri": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Montana": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Nebraska": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Nevada": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "New Hampshire": ["Robert Johnson", "Elizabeth Foster", "Sarah Thomas"],
        "New Jersey": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "New Mexico": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "New York": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "North Carolina": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "North Dakota": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Ohio": ["Sarah Thomas", "Elizabeth Foster", "Robert Johnson"],
        "Oklahoma": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Oregon": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Pennsylvania": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Rhode Island": ["Robert Johnson", "Elizabeth Foster", "Sarah Thomas"],
        "South Carolina": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "South Dakota": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Tennessee": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Texas": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Utah": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Vermont": ["Robert Johnson", "Elizabeth Foster", "Sarah Thomas"],
        "Virginia": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Washington": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "West Virginia": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"],
        "Wisconsin": ["Sarah Thomas", "Elizabeth Foster", "Robert Johnson"],
        "Wyoming": ["Elizabeth Foster", "Sarah Thomas", "Robert Johnson"]
    }
    return state_candidates


def getStateProbabilities():
    state_probabilities = {
        "Alabama": [0.6, 0.3, 0.1],
        "Alaska": [0.7, 0.2, 0.1],
        "Arizona": [0.5, 0.4, 0.1],
        "Arkansas": [0.6, 0.3, 0.1],
        "California": [0.5, 0.4, 0.1],
        "Colorado": [0.5, 0.4, 0.1],
        "Connecticut": [0.6, 0.2, 0.2],
        "Delaware": [0.5, 0.3, 0.2],
        "Florida": [0.6, 0.3, 0.1],
        "Georgia": [0.6, 0.3, 0.1],
        "Hawaii": [0.6, 0.3, 0.1],
        "Idaho": [0.4, 0.3, 0.3],
        "Illinois": [0.5, 0.4, 0.1],
        "Indiana": [0.4, 0.3, 0.3],
        "Iowa": [0.3, 0.5, 0.2],
        "Kansas": [0.4, 0.4, 0.2],
        "Kentucky": [0.5, 0.4, 0.1],
        "Louisiana": [0.6, 0.3, 0.1],
        "Maine": [0.9, 0.05, 0.05],
        "Maryland": [0.4, 0.4, 0.2],
        "Massachusetts": [0.5, 0.3, 0.2],
        "Michigan": [0.4, 0.3, 0.3],
        "Minnesota": [0.3, 0.6, 0.1],
        "Mississippi": [0.6, 0.3, 0.1],
        "Missouri": [0.4, 0.4, 0.2],
        "Montana": [0.4, 0.3, 0.3],
        "Nebraska": [0.3, 0.5, 0.2],
        "Nevada": [0.5, 0.4, 0.1],
        "New Hampshire": [0.3, 0.5, 0.2],
        "New Jersey": [0.4, 0.3, 0.3],
        "New Mexico": [0.5, 0.3, 0.2],
        "New York": [0.4, 0.3, 0.3],
        "North Carolina": [0.6, 0.3, 0.1],
        "North Dakota": [0.3, 0.5, 0.2],
        "Ohio": [0.4, 0.3, 0.3],
        "Oklahoma": [0.6, 0.3, 0.1],
        "Oregon": [0.5, 0.4, 0.1],
        "Pennsylvania": [0.5, 0.4, 0.1],
        "Rhode Island": [0.3, 0.5, 0.2],
        "South Carolina": [0.6, 0.3, 0.1],
        "South Dakota": [0.4, 0.4, 0.2],
        "Tennessee": [0.7, 0.2, 0.1],
        "Texas": [0.6, 0.3, 0.1],
        "Utah": [0.4, 0.3, 0.3],
        "Vermont": [0.3, 0.5, 0.2],
        "Virginia": [0.5, 0.4, 0.1],
        "Washington": [0.5, 0.3, 0.2],
        "West Virginia": [0.6, 0.3, 0.1],
        "Wisconsin": [0.4, 0.3, 0.3],
        "Wyoming": [0.4, 0.3, 0.3]
    }
    return state_probabilities




def candidatePickr(state):
    candidate_list = getStateCandidates()[state]
    probability_list = getStateProbabilities()[state]
    chosen_cadidate = random.choices(candidate_list, probability_list)
    return chosen_cadidate

def partyPicker(candidate):

    if candidate == "Robert Johnson":
        party = random.choices(getParties(), [0.9, 0.05, 0, 0.05])
    elif candidate == "Elizabeth Foster":
        party = random.choices(getParties(), [0.1, 0.8, 0, 0.1])
    elif candidate == "Sarah Thomas":
        party = random.choices(getParties(), [0.05, 0.05, 0.5, 0.4])
    return party





def generate(num_records):
    f = open("election_data.txt", "w")
    for _ in range(num_records):
        first_name = random.choice(getFirstName())
        last_name = random.choice(getLastName())
        state = random.choice(getStates())
        candidate = candidatePickr(state)[0]
        party = partyPicker(candidate)[0]
        line = f"{first_name} {last_name} {state} {party} {candidate}\n"
        f.write(line)


generate(10000)