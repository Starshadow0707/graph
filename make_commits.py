import random
import os

# zalgoification stolen from a code golf example, could I format this better? yes. will I? no.
q=lambda z:''.join([v,v+''.join(random.choice(list(map(chr,range(768,815))))for i in range(int(random.normalvariate(10,5))))][v.isalpha()]for v in z)

# these messages taken from a list of most common commit messages
messages=[
	"initial commit",
	"update readme.md",
	"update",
	"first commit",
	"dummy",
	"updated readme",
	"pi push",
	"create readme.md",
	"fix",
	"cleanup",
	"test",
	"typo",
	"fuck",
	"wip",
	"bump version",
	"updates"	
]

# I couldn't get the bash for loop to run in the github action, so... here we are.
for n in range(random.randint(1, 10)):
	message = q(random.choice(messages))
	os.system(f'git commit -m "{message}" --allow-empty')










class Solution {
public:
    Node* reverse(Node* head) {
        Node* prev = nullptr;
        Node* curr = head;
        while (curr) {
            Node* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    Node* addTwoLists(Node* l1, Node* l2) {
        l1 = reverse(l1);
        l2 = reverse(l2);
        Node* dummy = new Node(0);
        Node* tail = dummy;
        int carry = 0;
        while (l1 || l2 || carry) {
            int sum = carry;
            if (l1) sum += l1->data, l1 = l1->next;
            if (l2) sum += l2->data, l2 = l2->next;
            carry = sum / 10;
            tail->next = new Node(sum % 10);
            tail = tail->next;
        }
        Node* res = reverse(dummy->next);
        delete dummy;
        while (res && res->data == 0 && res->next) {
            Node* temp = res;
            res = res->next;
            delete temp;
        }
        return res;
    }
};
