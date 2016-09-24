import heapq
import numpy as np

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
        if colorHistState is True:
            allScores = final_scores[img_id]
            scoreColorHist = allScores.get("colorHist", 1) 

            maxScore = results_color_hist[len(results_color_hist)-1][0]
            minScore = results_color_hist[0][0]
            if maxScore == minScore: # Has vk scores but all the same
                scoreColorHist = 0.5
            else:
                if len(results_color_hist) > 1:
                    scoreColorHist = (scoreColorHist - minScore) / (maxScore - minScore)
            scoreColorHist *= weights["colorHistWeight"] / sumWeights

        if vkState is True:
            allScores = final_scores[img_id]
            vkScore = allScores.get("sift", 1) 

            maxScore = results_sift[len(results_sift)-1][0]
            minScore = results_sift[0][0]
            if maxScore == minScore: # Has vk scores but all the same
                vkScore = 0.5
            else:
                if len(results_sift) > 1:
                    vkScore = (vkScore - minScore) / (maxScore - minScore)
            vkScore *= weights["vkWeight"] / sumWeights

        if vcState is True:
            allScores = final_scores[img_id]
            vcScore = allScores.get("visualConcept", 1) 

            maxScore = results_visual_concept[len(results_visual_concept)-1][0]
            minScore = results_visual_concept[0][0]
            if maxScore == minScore: # Has vk scores but all the same
                vcScore = 0.5
            else:
                if len(results_visual_concept) > 1:
                    vcScore = (vcScore - minScore) / (maxScore - minScore)

            vcScore *= weights["vcWeight"] / sumWeights
        
        if dpLearnState is True:
            allScores = final_scores[img_id]
            dlScore = allScores.get("deepLearn", 1)

            maxScore = results_deep_learn[len(results_deep_learn)-1][0]
            minScore = results_deep_learn[0][0]
            if maxScore == minScore: # Has vk scores but all the same
                dlScore = 0.5
            else:
                if len(results_deep_learn) > 1:
                    dlScore = (dlScore - minScore) / (maxScore - minScore)

            dlScore *= weights["dpLearnWeight"] / sumWeights

        if textState is True:
            allScores = final_scores[img_id]
            textScore = allScores.get("text", 1) 

            maxScore = results_text[len(results_text)-1][0]
            minScore = results_text[0][0]
            if maxScore == minScore: # Has vk scores but all the same
                textScore = 0.5
            else:
                if len(results_text) > 1:
                    textScore = (textScore - minScore) / (maxScore - minScore)

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
