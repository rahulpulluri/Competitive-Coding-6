# Time Complexity : O(1)
# - For each message, we do a dictionary lookup and update — constant time.
#
# Space Complexity : O(n)
# - Where n is the number of unique messages in the lifetime of the logger.
# - Each message has a timestamp stored in the dictionary.

# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : No


# Tradeoff: Unbounded memory if messages keep coming infinitely with new content.
# Ideal when:
# - You want ultra-fast lookups (O(1))
# - High-throughput environments (like logging systems or message brokers)

class Logger:

    def __init__(self):
        # HashMap: message → next allowed timestamp
        self.log_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.log_dict or timestamp - self.log_dict[message] >= 10:
            self.log_dict[message] = timestamp
            return True
        return False


# ------------------------------------------------------------
# 📝 Approach 2: Queue + Set (bounded memory sliding window)
# Time Complexity : Amortized O(1)
# - We only remove old entries and add new ones in the queue.
# Space Complexity : O(k)
# - k = number of unique messages in any 10-second window
#
# Best when you want to automatically forget old data and avoid memory leaks.

# from collections import deque
# class Logger:
#     def __init__(self):
#         self.msg_queue = deque()
#         self.msg_set = set()
#
#     def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
#         while self.msg_queue:
#             old_msg, old_time = self.msg_queue[0]
#             if timestamp - old_time >= 10:
#                 self.msg_queue.popleft()
#                 self.msg_set.remove(old_msg)
#             else:
#                 break
#         if message not in self.msg_set:
#             self.msg_set.add(message)
#             self.msg_queue.append((message, timestamp))
#             return True
#         return False


# ------------------------------------------------------------
# 📝 Approach 3: Naive List Approach
# Time Complexity : O(n)
# - We scan the list every time to check for recent duplicates.
# Space Complexity : O(n)
# - n = total number of logs stored (unbounded).
#
# Not suitable for high-frequency systems. Useful for understanding brute force.

# class Logger:
#     def __init__(self):
#         self.logs = []
#
#     def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
#         for t, msg in reversed(self.logs):
#             if msg == message and timestamp - t < 10:
#                 return False
#         self.logs.append((timestamp, message))
#         return True


# ------------------------------------------------------------
if __name__ == "__main__":
    logger = Logger()
    print(logger.shouldPrintMessage(1, "foo"))   # True
    print(logger.shouldPrintMessage(2, "bar"))   # True
    print(logger.shouldPrintMessage(3, "foo"))   # False
    print(logger.shouldPrintMessage(8, "bar"))   # False
    print(logger.shouldPrintMessage(10, "foo"))  # False
    print(logger.shouldPrintMessage(11, "foo"))  # True
