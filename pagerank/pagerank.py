import os
import random
import re
import sys
import numpy as np
DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    #print(corpus)
    #print(transition_model(corpus, list(corpus.keys())[0], DAMPING))
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    avail = corpus[page]
    probability = {}
    if len(avail) == 0:
        prob_page = 1/len(corpus.keys())
    else:
        prob_page = (1-damping_factor)/len(corpus.keys())
        prob_link = damping_factor/len(avail)
        
    for page in corpus.keys():
        if page in avail:
            probability[page] = prob_page+prob_link
        else:
            probability[page] = prob_page
                
                
                
    return probability   
        
        
    
    
    #raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.
    
    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page = random.choice(list(corpus.keys()))
    sample = []
    sample.append(page)
    
    
    for i in range(n):
        current_page = sample[i]
        probabilities = transition_model(corpus, current_page, damping_factor)
        next_page = np.random.choice(list(probabilities.keys()), p=list(probabilities.values()))
        sample.append(next_page)
    
    dict_page = {}
    for page in corpus.keys():
        dict_page[page] = sample.count(page)/len(sample)
    return dict_page
        
    
    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {}
    for page in corpus.keys():
        pagerank[page] = 1/len(corpus.keys())
    
    prev_rank = pagerank.copy()
    flg = dict([(key, False) for key in prev_rank.keys()])
    
    while True:
        
        for page in corpus.keys():
            prob_1 = (1-damping_factor)/len(corpus.keys())
            
            prob_2 = 0
            for prev_page, page_links in corpus.items():
                if len(page_links) == 0:
                    page_links = corpus.keys()
                if page in page_links:
                    prob_2 += prev_rank[prev_page]/len(page_links)
                    
            final_prob = prob_1 + damping_factor*prob_2
            pagerank[page] = final_prob
        
        
    
        for page in prev_rank.keys():
            if abs(prev_rank[page] - pagerank[page]) < 0.001:
                flg[page] = True
            else:
                flg[page] = False
        if all(flg.values()):
            break
        prev_rank = pagerank.copy()
    return pagerank
    raise NotImplementedError


if __name__ == "__main__":
    main()
