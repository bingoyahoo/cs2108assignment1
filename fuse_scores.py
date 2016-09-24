import heapq
import numpy as np

def normalize_score(score, results):
        """Normalises score to 0(best) -> 1(worst)"""
        if len(results) == 0:
            return 0.5
        normalized_score = score
        maxScore = results[len(results)-1][0]
        minScore = results[0][0]
        if maxScore == minScore: # Has vk scores but all the same
            normalized_score = 0.5
        else:
            if len(results) > 1:
                normalized_score = (normalized_score - minScore) / (maxScore - minScore)
        return normalized_score


def fuse_scores(statesConfiguration, weights, results_color_hist, results_sift, results_text, results_deep_learn, results_visual_concept):
    # finalresults has {img_id -> 5 dictionaries for the features score}, namely color hist, keyword
    # visual concept, text and deep learning
    final_scores = {}

    colorHistState = statesConfiguration["colorHist"]
    vcState = statesConfiguration["visualConcept"]
    vkState = statesConfiguration["visualKeyword"]
    dpLearnState = statesConfiguration["deepLearning"]
    textState = True if len(results_text) > 0 else False

    sumWeights = 0
    if colorHistState is True:
        sumWeights += weights["colorHistWeight"]
    if vkState is True:
        sumWeights += weights["vkWeight"]
    if vcState is True:
        sumWeights += weights["vcWeight"]
    if dpLearnState is True:
        sumWeights += weights["dpLearnWeight"]
    if textState is True:
        sumWeights += weights["textWeight"]

    # Inserts score
    for score, img_id in results_color_hist:
        if img_id not in final_scores:
            final_scores[img_id] = {}
        final_scores[img_id]["colorHist"] = score

    for score, img_id in results_sift:
        if img_id not in final_scores:
            final_scores[img_id] = {}
        final_scores[img_id]["sift"] = score

    for score, img_id in results_text:
        if img_id not in final_scores:
            final_scores[img_id] = {}
        final_scores[img_id]["text"] = score

    for score, img_id in results_deep_learn:
        if img_id not in final_scores:
            final_scores[img_id] = {}
        final_scores[img_id]["deepLearn"] = score

    for score, img_id in results_visual_concept:
        if img_id not in final_scores:
            final_scores[img_id] = {}
        final_scores[img_id]["visualConcept"] = score

    print "Sum weights ", sumWeights

    heap_scores = []
    for img_id in final_scores:
        scoreColorHist = vkScore = vcScore = dlScore = textScore = 1
        allScores = final_scores[img_id]
        if colorHistState is True:
            scoreColorHist = allScores.get("colorHist", results_color_hist[len(results_color_hist)-1][0]) 
            scoreColorHist = normalize_score(scoreColorHist, results_color_hist)
            scoreColorHist *= weights["colorHistWeight"] / sumWeights

        if vkState is True:
            vkScore = allScores.get("sift", results_sift[len(results_sift)-1][0]) 
            vkScore = normalize_score(vkScore, results_sift)            
            vkScore *= weights["vkWeight"] / sumWeights

        if vcState is True:
            if len(results_visual_concept) != 0:
                vcScore = allScores.get("visualConcept", results_visual_concept[len(results_visual_concept)-1][0]) 
            vcScore = normalize_score(vcScore, results_visual_concept)            
            vcScore *= weights["vcWeight"] / sumWeights
        
        if dpLearnState is True:
            dlScore = allScores.get("deepLearn", results_deep_learn[len(results_deep_learn)-1][0])
            dlScore = normalize_score(dlScore, results_deep_learn)            
            dlScore *= weights["dpLearnWeight"] / sumWeights

        if textState is True:
            textScore = allScores.get("text", results_text[len(results_text)-1][0]) 
            textScore = normalize_score(textScore, results_text)            
            textScore *= weights["textWeight"] / sumWeights

        sumScore = scoreColorHist + vkScore + vcScore + dlScore + textScore
        heapq.heappush(heap_scores, (sumScore, img_id)) # push (sumScore, img_id) into heap
    
    topResult = heapq.nsmallest(16, heap_scores)
    return topResult, final_scores

def main():
    list1 = [(0.25, "abc")]
    list2 = [(0.25, "abc"), (0.50, "def")]
    list3 = [(0.25, "abc"), (0.50, "def")]
    list4 = [(0.25, "abc"), (0.50, "def")]
    list5 = [(0.25, "abc"), (0.50, "def")]
    statesConfiguration = {"colorHist": True, "visualConcept": True, "visualKeyword": True, "deepLearning": True}
    fuse_scores(statesConfiguration, list1, list2, list3, list4, list5)


if __name__ == '__main__':
    main()
