import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue
        itr = 0
        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                
                if itr == 0:
                    itr+=1
                    #print(probabilities)
                update(probabilities, one_gene, two_genes, have_trait, p)
                if  itr == 1:
                    itr+=1
                    #print('after update', probabilities)
    # Ensure probabilities sum to 1
    #print(probabilities)
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    probs = 1
    
    for person in people.keys():
        trait = False
        if person in have_trait:
            trait = True
        
            
            
        genes = 0
        if person in one_gene:
            genes = 1
        elif person in two_genes:
            genes = 2
            
        probability = 0   
        
        
        
        # first check whether the person has parent or not if not calculate with conditional prob.
        if not people[person]['mother'] and not people[person]['father']:
            probability = PROBS["gene"][genes] * PROBS["trait"][genes][trait]
            
            #if person has parent pass gene with mutation and apply conditional prob.
        else:
            
            gene_mother = False
            if people[person]['mother'] in one_gene or people[person]['mother'] in two_genes:
                gene_mother = True
                
            gene_father = False
            if people[person]['father'] in one_gene or people[person]['father'] in two_genes:
                gene_father = True
            
            probability_gene = 0
            
            one_parent_gene_mutate = PROBS['mutation']*(1-PROBS['mutation'])*2
            both_parent_gene_not_mutate = (1-PROBS["mutation"])**2 *2
            both_parent_gene_mutate = PROBS['mutation']**2 *2
            
            if genes == 1:
                if gene_father or gene_mother:
                    probability_gene = PROBS['mutation']**2 + (1-PROBS['mutation'])**2       #1 parent has gene
                    #print('1 parent',probability_gene)
                elif gene_father and gene_mother:
                    probability_gene = PROBS['mutation']*(1-PROBS['mutation'])*2  #it can be replaced with one_parent_gene_mutate          #both parent has gene
                    #print('2 parent')
                elif not gene_mother and not gene_father:
                    probability_gene = one_parent_gene_mutate          #no parent has gene
                    #print('zero parent')
            elif genes == 2:
                if gene_father or gene_mother:
                    probability_gene = one_parent_gene_mutate
                elif gene_mother and gene_father:
                    probability_gene = both_parent_gene_not_mutate
                elif not gene_mother and not gene_father:
                    probability_gene = both_parent_gene_mutate
            else:
                if gene_father or gene_mother:
                    probability_gene = one_parent_gene_mutate
                elif not gene_mother and not gene_father:
                    probability_gene = both_parent_gene_not_mutate
                elif gene_mother and gene_father:
                    probability_gene = both_parent_gene_mutate
           
            
            #print('gene no and prob trait', genes, PROBS["trait"][genes][trait])
            probability = probability_gene * PROBS["trait"][genes][trait]             #probability that it has now trait or not with gene +1 genes
            
        #print(f' your {person} with {probability}')
        probs *= probability
    return probs
    
    
    
    
            
    
    
    raise NotImplementedError


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    
    for person in set(probabilities):
        gene = 0
        if person in one_gene:
            gene = 1
        if person in two_genes:
            gene = 2
        probabilities[person]['gene'][gene]+=p
        trait = False
        if person in have_trait:
            trait = True
        probabilities[person]['trait'][trait]+=p
        
        
        
    #raise NotImplementedError


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in set(probabilities):
        
        
        #normalize gene data
        k = sum(list(probabilities[person]['gene'].values()))
        if k != 0:
            k = 1/k
            for gene in probabilities[person]['gene']:
                probabilities[person]['gene'][gene] *= k
        #print('sum is',sum(list(probabilities[person]['gene'].values())))
        k = sum(list(probabilities[person]['trait'].values()))
        if k != 0:
            k = 1/k
        #normalize trait data
        for trait in probabilities[person]['trait']:
            probabilities[person]['trait'][trait] *= k
        
        
        
    
    
    
    
    #raise NotImplementedError


if __name__ == "__main__":
    main()
