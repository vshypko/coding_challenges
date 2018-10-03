def textQueries(sentences, queries):
    # SOLUTION 1 (using maps, no implementation for multiple occurences, times out)
    #     query_words_list = list()

    #     query_words_map = {}
    #     sentence_words_map = {}
    #     results_map = {}

    #     for query in queries:
    #         query_words_list.append(query.split())

    #     for i in range(len(queries)):
    #         query_words = queries[i].split()
    #         for word in query_words:
    #             if word not in query_words_map.keys():
    #                 query_words_map[word] = [i]
    #             else:
    #                 query_words_map[word] += [i]

    #     for i in range(len(sentences)):
    #         sentence_words = sentences[i].split()
    #         for word in set(sentence_words):
    #             if word not in sentence_words_map.keys():
    #                 sentence_words_map[word] = [(i, sentence_words.count(word))]
    #             else:
    #                 sentence_words_map[word] += [(i, sentence_words.count(word))]

    #     for query_word, query_ids in query_words_map.items():
    #         for q_id in query_ids:
    #             if query_word in sentence_words_map.keys():
    #                 for pair in sentence_words_map[query_word]:
    #                     if q_id not in results_map.keys():
    #                         results_map[q_id] = [(pair)]
    #                     else:
    #                         results_map[q_id] += [(pair)]

    #     for i in range(len(queries)):
    #         results = ""
    #         for j in range(len(sentences)):
    #             sentence_counter = 0
    #             if i in results_map.keys():
    #                 for item in results_map[i]:
    #                     if item[0] == j:
    #                         sentence_counter += 1
    #                 if sentence_counter >= len(query_words_list[i]):
    #                     results += str(j) + " "
    #         if results != "":
    #             print(results)
    #         else:
    #             print(-1)

    # SOLUTION 2: iterating over sentences / queries
    #     results = list()

    #     query_words_list = list()
    #     sentence_words_list = list()

    #     for query in queries:
    #         query_words_list.append(query.split())
    #         results.append("")

    #     for sentence in sentences:
    #         sentence_words_list.append(sentence.split())

    #     for i in range(len(sentence_words_list)):
    #         current_sentence = sentence_words_list[i]
    #         for j in range(len(query_words_list)):
    #             first_query_word = query_words_list[j][0]
    #             current_word_counter = current_sentence.count(first_query_word)
    #             for word in query_words_list[j]:
    #                 count_word = current_sentence.count(word)
    #                 current_word_counter = min(current_word_counter, count_word)
    #                 if current_word_counter == 0:
    #                     break
    #             for k in range(current_word_counter):
    #                 results[j] += str(i) + " "
    #     results = [result if result != "" else "-1" for result in results]
    #     for result in results:
    #         print(result)

    results = list()
    for query in queries:
        current_query_result = ""
        words = query.split()
        for i in range(len(sentences)):
            sentence_in_words = sentences[i].split()
            current_word_counter = sentence_in_words.count(words[0])
            for word in words:
                current_word_times = sentence_in_words.count(word)
                current_word_counter = min(current_word_counter, current_word_times)
            if current_word_counter >= 1:
                for j in range(current_word_counter):
                    current_query_result += str(i) + " "
        if len(current_query_result) > 0:
            results.append(current_query_result)
        else:
            results.append("-1")
    for result in results:
        print(result)


sentences = list()
sentences.append("bob and alice like to text each other")
sentences.append("bob does not like to ski but does not like to fall")
sentences.append("alice likes to ski")

queries = list()
queries.append("bob alice")
queries.append("alice")
queries.append("like")

textQueries(sentences, queries)
