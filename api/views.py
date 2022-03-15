from rest_framework.decorators import api_view
from rest_framework.response import Response
from questions.models import Question
from .serializer import QuestionSerializer

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        # Question
        'List-question': '/question-list/',
        'Detail-question': '/question-detail/<str:pk>/',
        'Create-question': '/question-create/',
        'Update-question': '/question-update/<str:pk>/',
        'Delete-question': '/question-delete/<str:pk>/',

        # Video
    }
    return Response(api_urls)

@api_view(['GET'])
def question_list(request):
    """List all questions"""
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def question_detail(request, pk):
    """Detailed view of a question"""
    question = Question.objects.get(id=pk)
    serializer = QuestionSerializer(question, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def question_create(request):
    """create a question"""
    data = request.data
    serializer = QuestionSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def question_update(request, pk):
    """update a question"""
    question = Question.objects.get(id=pk)
    if request.method == 'POST':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
    else:
        serializer = QuestionSerializer(question)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def question_delete(request, pk):
    """delete a question"""
    question = Question.objects.get(id=pk)
    if request.method == 'DELETE':
        response = f'Deleted <{question}>'
        question.delete()
        return Response(response)
    serializer = QuestionSerializer(question)
    return Response(serializer.data)
