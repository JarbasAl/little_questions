from sklearn.linear_model import RidgeClassifier
from little_questions.classifiers import QuestionClassifier, SimpleQuestionClassifier


class RidgeQuestionClassifier(QuestionClassifier):
    def __init__(self, name="ridge"):
        super().__init__(name)

    @property
    def classifier_class(self):
        return RidgeClassifier(solver="lbfgs")


class SimpleRidgeQuestionClassifier(RidgeQuestionClassifier, SimpleQuestionClassifier):
    def __init__(self, name="ridge_main"):
        super().__init__(name)


if __name__ == '__main__':
    train = True
    search = False
    clf = SimpleRidgeQuestionClassifier()
    if search:
        t, tt = clf.load_data()
        clf.grid_search(t, tt)
    if train:
        t, tt = clf.load_data()

        clf.train(t, tt)
        clf.save()
    else:
        clf.load()
    # model performance
    # Accuracy: Accuracy: 0.768
    clf.evaluate_model()

    # visual inspection

    questions = ["what do dogs and cats have in common",
                 "tell me about evil",
                 "how to kill animals ( a cow ) and make meat",
                 "what is a living being",
                 "why are humans living beings",
                 "give examples of animals",
                 "what is the speed of light",
                 "when were you born",
                 "where do you store your data",
                 "will you die",
                 "have you finished booting",
                 "should i program artificial stupidity",
                 "who made you",
                 "how long until sunset",
                 "how long ago was sunrise",
                 "how much is bitcoin worth",
                 "which city has more people",
                 "whose dog is this",
                 "did you know that dogs are animals",
                 "do you agree that dogs are animals",
                 "what time is it?",
                 "not a question"]
    # for q in questions:
    #    print(q, clf.predict([q]))