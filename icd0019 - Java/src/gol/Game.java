package gol;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.function.Supplier;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Game {
    private List<List<Boolean>> gameboard = new ArrayList<>();

    public void genEmptyGameboard(int x, int y) {
        for (int ycord = 0; ycord <= y; ycord++) {
            List<Boolean> line = new ArrayList<>();
            IntStream.range(0, x + 1).forEach(l -> {
                line.add(false);
            });
            gameboard.add(line);
        }
        gameboard.get(y).set(x, true);
    }

    public void adjustBoard(int x, int y) {
        var maxLineLen = Collections.max(gameboard.stream().map(List::size).toList());
        maxLineLen = Math.max(maxLineLen, x + 1);
        var lines = Math.max(gameboard.size(), y + 1);
        for (int ycord = 0; ycord < lines; ycord++) {
            for (int xcord = 0; xcord < maxLineLen; xcord++) {
                try {
                    gameboard.get(ycord).get(xcord);
                } catch (java.lang.IndexOutOfBoundsException e) {
                    try {
                        gameboard.get(ycord);
                    } catch (java.lang.IndexOutOfBoundsException e0) {
                        List<Boolean> line = new ArrayList<>();
                        IntStream.range(0, maxLineLen).forEach(l -> line.add(false));
                        gameboard.add(line);
                    }
                    try {
                        gameboard.get(ycord).get(xcord);
                    } catch (java.lang.IndexOutOfBoundsException e0) {
                        var line = gameboard.get(ycord);
                        while (line.size() != maxLineLen) {
                            line.add(false);
                        }
                        gameboard.set(ycord, line);
                    }
                }
            }
        }
    }

    public void markAlive(int x, int y) {
        if (gameboard.isEmpty()) {
            genEmptyGameboard(x, y);
            return;
        }
        adjustBoard(x, y);
        gameboard.get(y).set(x, true);

    }

    public boolean isAlive(int x, int y) {
        try {
            return gameboard.get(y).get(x);
        } catch (java.lang.IndexOutOfBoundsException e) {
            markAlive(x, y);
            toggle(x, y);
        }
        return gameboard.get(y).get(x);
    }

    public void toggle(int x, int y) {
        gameboard.get(y).set(x, !gameboard.get(y).get(x));
    }

    public Integer getNeighbourCount(int x, int y) {
        int neighbourCount = 0;
        List<List<Integer>> coordinates = new ArrayList<>();

        var arr = new ArrayList<Integer>();
        arr.add(0, x - 1);
        arr.add(1, y - 1);
        coordinates.add(arr.stream().toList());
        arr.clear();

        arr.add(0, x);
        arr.add(1, y - 1);
        coordinates.add(arr.stream().toList());
        arr.clear();
        arr.add(0, x + 1);
        arr.add(1, y - 1);
        coordinates.add(arr.stream().toList());
        arr.clear();

        arr.add(0, x - 1);
        arr.add(1, y);
        coordinates.add(arr.stream().toList());
        arr.clear();

        arr.add(0, x + 1);
        arr.add(1, y);
        coordinates.add(arr.stream().toList());
        arr.clear();

        arr.add(0, x - 1);
        arr.add(1, y + 1);
        coordinates.add(arr.stream().toList());
        arr.clear();

        arr.add(0, x);
        arr.add(1, y + 1);
        coordinates.add(arr.stream().toList());
        arr.clear();

        arr.add(0, x + 1);
        arr.add(1, y + 1);
        coordinates.add(arr.stream().toList());
        arr.clear();

        for (List<Integer> coord : coordinates) {
            try {
                if (gameboard.get(coord.get(1)).get(coord.get(0))) {
                    neighbourCount += 1;
                }
            } catch (Exception e) {
            }
        }
        return neighbourCount;
    }

    public void nextFrame() {
        List<List<Boolean>> emptyBoard = new ArrayList<>();
        IntStream.range(0, gameboard.size() + 1).forEach(l -> {
            List<Boolean> line = new ArrayList<>();
            IntStream.range(0, gameboard.get(0).size() + 1).forEach(cell -> {
                line.add(false);
            });
            emptyBoard.add(line);
        });
        for (int y = 0; y < emptyBoard.size(); y++) {
            for (int x = 0; x < emptyBoard.get(0).size(); x++) {
                var neighbourC = getNeighbourCount(x, y);
                boolean live;
                try {
                    live = gameboard.get(y).get(x);
                } catch (java.lang.IndexOutOfBoundsException e) {
                    live = false;
                }
                var nextS = nextState(live, neighbourC);
                emptyBoard.get(y).set(x, nextS);
            }
        }
        gameboard = emptyBoard;
    }

    public void clear() {
        gameboard.clear();
    }

    public boolean nextState(boolean isLiving, int neighborCount) {
        if (!isLiving && neighborCount == 3) {
            return true;
        }
        return isLiving && (neighborCount == 2 || neighborCount == 3);
    }
}
