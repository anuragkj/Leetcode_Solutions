# [2409] Count Days Spent Together

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-10-24 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/count-days-spent-together/)

**Topics:** Math, String

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

Example 1:

Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.

Example 2:

Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
Output: 0
Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.

Constraints:

- All dates are provided in the format "MM-DD".

- Alice and Bob's arrival dates are earlier than or equal to their leaving dates.

- The given dates are valid dates of a non-leap year.

**Examples / sample tests:**

```
"08-15"
"08-18"
"08-16"
"08-19"
"10-01"
"10-31"
"11-01"
"12-31"
```

---

## Problem Summary
Alice and Bob are traveling to Rome, each for a specific period. We are given their arrival and departure dates (inclusive) in "MM-DD" format. The goal is to calculate the total number of days they are both in Rome together, assuming all dates are in the same non-leap year.

## Intuition
The problem asks for the number of overlapping days between two time intervals. This is a classic interval intersection problem. Dates can be tricky to compare directly, so a good first step is to convert them into a simpler, comparable format. Since all dates are within the same non-leap year, we can convert each "MM-DD" date into a **day number** (e.g., January 1st is day 1, January 2nd is day 2, and so on, up to December 31st being day 365). Once dates are represented as simple integers, finding the overlap becomes straightforward.

## Approach
The optimal approach involves converting all dates to a single numerical representation (day number) and then applying standard interval intersection logic.

1.  **Precompute Cumulative Days**: Create a list or array that stores the number of days *before* each month. This will help quickly convert "MM-DD" to a day number.
    *   The given days per month are `[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]` (January is month 0, February is month 1, etc.).
    *   Let's create a `prefix_sum_days` list:
        *   `prefix_sum_days[0]` = 0 (days before January)
        *   `prefix_sum_days[1]` = 31 (days before February)
        *   `prefix_sum_days[2]` = 31 + 28 = 59 (days before March)
        *   ...and so on, up to `prefix_sum_days[12]` = 365 (total days in the year).

2.  **Helper Function `date_to_day_number(date_str)`**:
    *   This function will take a date string like "MM-DD".
    *   Parse the month `MM` and day `DD` as integers.
    *   The day number for `MM-DD` will be `prefix_sum_days[MM - 1] + DD`. (We use `MM - 1` because `prefix_sum_days` is 0-indexed for months, but `MM` is 1-indexed).

3.  **Convert All Dates**: Use the `date_to_day_number` helper function to convert `arriveAlice`, `leaveAlice`, `arriveBob`, and `leaveBob` into their respective day numbers:
    *   `alice_arrival_day`
    *   `alice_leave_day`
    *   `bob_arrival_day`
    *   `bob_leave_day`

4.  **Find Overlap Interval**:
    *   The **start of the overlapping period** is the later of the two arrival dates: `start_overlap = max(alice_arrival_day, bob_arrival_day)`.
    *   The **end of the overlapping period** is the earlier of the two leave dates: `end_overlap = min(alice_leave_day, bob_leave_day)`.

5.  **Calculate Overlap Days**:
    *   The number of days in the overlap interval is `end_overlap - start_overlap + 1`.
    *   **Important**: If `start_overlap > end_overlap`, it means there is no actual overlap (the intervals don't touch or cross). In this case, the number of overlapping days is 0. We can handle this by taking `max(0, end_overlap - start_overlap + 1)`.

## Visualization
Imagine a timeline where each day is a point. Alice and Bob's trips are intervals on this timeline.

```
Timeline (Day numbers)
Day 1                                                                     Day 365
|-----------------------------------------------------------------------------|

Alice's trip:   [ alice_arrival_day . . . . . . . . . alice_leave_day ]
                ^                                   ^

Bob's trip:             [ bob_arrival_day . . . . . . . . . bob_leave_day ]
                        ^                                   ^

Overlap:                [ start_overlap . . . . . . . . . end_overlap ]
                        ^                               ^
                        max(alice_arrival_day, bob_arrival_day)
                                                        min(alice_leave_day, bob_leave_day)
```

## Dry Run
Let's walk through **Example 1**:
`arriveAlice = "08-15"`, `leaveAlice = "08-18"`
`arriveBob = "08-16"`, `leaveBob = "08-19"`

1.  **Precompute `prefix_sum_days`**:
    `days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`
    `prefix_sum_days = [0]`
    `current_sum = 0`
    `for days in days_in_month:`
        `current_sum += days`
        `prefix_sum_days.append(current_sum)`
    Result: `prefix_sum_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]`

2.  **Convert Dates to Day Numbers**:
    *   `arriveAlice = "08-15"`: Month=8, Day=15. `prefix_sum_days[8-1] + 15 = prefix_sum_days[7] + 15 = 212 + 15 = 227`.
        `alice_arrival_day = 227`
    *   `leaveAlice = "08-18"`: Month=8, Day=18. `prefix_sum_days[7] + 18 = 212 + 18 = 230`.
        `alice_leave_day = 230`
    *   `arriveBob = "08-16"`: Month=8, Day=16. `prefix_sum_days[7] + 16 = 212 + 16 = 228`.
        `bob_arrival_day = 228`
    *   `leaveBob = "08-19"`: Month=8, Day=19. `prefix_sum_days[7] + 19 = 212 + 19 = 231`.
        `bob_leave_day = 231`

3.  **Find Overlap Interval**:
    *   `start_overlap = max(alice_arrival_day, bob_arrival_day) = max(227, 228) = 228`
    *   `end_overlap = min(alice_leave_day, bob_leave_day) = min(230, 231) = 230`

4.  **Calculate Overlap Days**:
    *   `result = end_overlap - start_overlap + 1`
    *   `result = 230 - 228 + 1 = 3`
    *   Since `start_overlap` (228) is not greater than `end_overlap` (230), the `max(0, ...)` check passes.

**Final Result**: 3

## Complexity
*   **Time Complexity**: **O(1)**. We iterate through a fixed number of months (12) once to precompute `prefix_sum_days`, and then perform a fixed number of string parsing and arithmetic operations (4 date conversions, 2 `max`/`min` calls, 1 subtraction). The input size (date strings) is constant.
*   **Space Complexity**: **O(1)**. We store a fixed-size list (`prefix_sum_days` of length 13) and a few variables. The space used does not grow with the input.

## Edge Cases
*   **No Overlap (Example 2)**: If Alice leaves before Bob arrives, or vice-versa.
    *   `arriveAlice = "10-01"` (Day 274), `leaveAlice = "10-31"` (Day 304)
    *   `arriveBob = "11-01"` (Day 305), `leaveBob = "12-31"` (Day 365)
    *   `start_overlap = max(274, 305) = 305`
    *   `end_overlap = min(304, 365) = 304`
    *   `result = max(0, 304 - 305 + 1) = max(0, 0) = 0`. Correctly handled by `max(0, ...)`.
*   **One interval completely contains another**: E.g., Alice is in Rome from Jan 1 to Dec 31, Bob from Feb 1 to Feb 28.
    *   `start_overlap = max(1, 32) = 32` (Feb 1)
    *   `end_overlap = min(365, 59) = 59` (Feb 28)
    *   `result = 59 - 32 + 1 = 28`. Correct.
*   **Single-day trips**: E.g., Alice arrives and leaves on "08-15".
    *   `alice_arrival_day = 227`, `alice_leave_day = 227`.
    *   If Bob also arrives and leaves on "08-15", `start_overlap = 227`, `end_overlap = 227`.
    *   `result = 227 - 227 + 1 = 1`. Correct.
*   **Dates are identical**: Both arrive and leave on the exact same dates. This is a special case of complete containment and is handled correctly.

## Solution

```python
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Days in each month for a non-leap year (Jan=0, Feb=1, ..., Dec=11)
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Precompute prefix sums to quickly get day number from MM-DD
        # prefix_sum_days[i] will store the total days BEFORE month i (0-indexed)
        # So, prefix_sum_days[0] = 0 (days before Jan)
        # prefix_sum_days[1] = 31 (days before Feb)
        # ...
        # prefix_sum_days[12] = 365 (days before next year)
        prefix_sum_days = [0] * 13
        for i in range(12):
            prefix_sum_days[i+1] = prefix_sum_days[i] + days_in_month[i]

        # Helper function to convert "MM-DD" string to a day number (1-indexed from Jan 1)
        def date_to_day_number(date_str: str) -> int:
            month = int(date_str[:2])  # MM part
            day = int(date_str[3:])    # DD part
            # The day number is the sum of days before this month + the day itself
            return prefix_sum_days[month - 1] + day

        # Convert all four dates to their respective day numbers
        alice_arrival_day = date_to_day_number(arriveAlice)
        alice_leave_day = date_to_day_number(leaveAlice)
        bob_arrival_day = date_to_day_number(arriveBob)
        bob_leave_day = date_to_day_number(leaveBob)

        # Find the start of the overlapping period
        # This is the later of the two arrival dates
        start_overlap = max(alice_arrival_day, bob_arrival_day)

        # Find the end of the overlapping period
        # This is the earlier of the two leave dates
        end_overlap = min(alice_leave_day, bob_leave_day)

        # Calculate the number of days in the overlap
        # If start_overlap > end_overlap, there's no overlap, so result should be 0.
        # Otherwise, it's end_overlap - start_overlap + 1 (inclusive count).
        return max(0, end_overlap - start_overlap + 1)

```

## Why This Works
This solution works by transforming the problem from comparing complex date strings to comparing simple integers representing days of the year. By converting all dates to a 1-indexed day number (e.g., Jan 1 = day 1, Dec 31 = day 365), we effectively map each person's trip to a numerical interval `[arrival_day, leave_day]`. The intersection of two intervals `[A_start, A_end]` and `[B_start, B_end]` is given by `[max(A_start, B_start), min(A_end, B_end)]`. If the calculated `max_start` is greater than `min_end`, the intervals do not overlap, and the number of days is 0. Otherwise, the number of overlapping days is simply `min_end - max_start + 1` (inclusive count). This method correctly handles all possible relative positions of the two date ranges.

---
<sub>Generated 2026-10-24 04:56 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
